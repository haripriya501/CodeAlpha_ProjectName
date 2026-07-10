import pickle
import numpy as np

from tensorflow.keras.models import load_model
from music21 import instrument, note, stream, chord

# Load trained model
model = load_model("model.keras")

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Create mappings
pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

# Random starting sequence
start = np.random.randint(0, len(notes) - 100)

pattern = [note_to_int[n] for n in notes[start:start + 100]]

prediction_output = []

# Generate 500 notes
for _ in range(500):

    prediction_input = np.reshape(pattern, (1, len(pattern), 1))
    prediction_input = prediction_input / float(n_vocab)

    prediction = model.predict(prediction_input, verbose=0)

    index = np.argmax(prediction)
    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(index)
    pattern = pattern[1:]

# Convert to MIDI
offset = 0
output_notes = []

for pattern in prediction_output:

    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")
        chord_notes = []

        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)

    else:

        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)

midi_stream.write("midi", fp="output/generated_music.mid")

print("Music generated successfully!")