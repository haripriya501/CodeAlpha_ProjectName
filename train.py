import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.utils import to_categorical

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

print("Total notes:", len(notes))

# Create vocabulary
pitchnames = sorted(set(notes))

n_vocab = len(pitchnames)

print("Unique notes:", n_vocab)

# Create mappings
note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

sequence_length = 100

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in sequence_in])
    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

print("Training patterns:", n_patterns)

# Reshape input
network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(n_vocab)

network_output = to_categorical(network_output)

print("Data prepared successfully!")
# Build LSTM Model
model = Sequential()

model.add(LSTM(
    512,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))

model.add(Dropout(0.3))

model.add(LSTM(512))

model.add(Dense(256, activation="relu"))

model.add(Dropout(0.3))

model.add(Dense(n_vocab, activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

print("Model Created Successfully!")

# Train Model
model.fit(
    network_input,
    network_output,
    epochs=10,
    batch_size=64
)

# Save Model
model.save("model.keras")

print("Training Completed!")
print("Model Saved Successfully!")