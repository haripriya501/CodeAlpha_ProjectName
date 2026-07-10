from music21 import converter, instrument, note, chord
import glob
import pickle

notes = []

for file in glob.glob("dataset/*.mid"):
    print("Reading:", file)

    midi = converter.parse(file)

    try:
        parts = instrument.partitionByInstrument(midi)
        notes_to_parse = parts.parts[0].recurse()
    except:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append(".".join(str(n) for n in element.normalOrder))

print("Total notes:", len(notes))

with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("Notes saved successfully!")