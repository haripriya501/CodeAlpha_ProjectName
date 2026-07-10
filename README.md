# 🎵 AI Music Generator

## 📌 Overview

The AI Music Generator is a deep learning project developed as part of the **CodeAlpha Internship**. This project uses an **LSTM (Long Short-Term Memory)** neural network to learn musical patterns from MIDI files and generate new melodies in MIDI format.

The generated music can be played using any MIDI-compatible media player or music software.

---

## ✨ Features

- 🎼 Reads and preprocesses MIDI music files
- 🧠 Trains an LSTM neural network on musical note sequences
- 🎵 Generates new AI-composed melodies
- 💾 Saves the generated music as a MIDI file
- ⚡ Simple and easy-to-understand Python implementation

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Music21
- NumPy
- MIDI Dataset

---

## 📂 Project Structure

```
Music_Generation_AI/
│
├── dataset/
├── output/
│   └── generated_music.mid
├── preprocess.py
├── train.py
├── generate.py
├── notes.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How to Run

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Preprocess the dataset

```bash
python preprocess.py
```

### 3. Train the AI model

```bash
python train.py
```

### 4. Generate music

```bash
python generate.py
```

The generated MIDI file will be saved in the **output** folder.

---

## 📸 Output

The generated music is saved as:

```
output/generated_music.mid
```

You can play it using any MIDI player or software such as VLC Media Player or MuseScore.

---

## 📖 Note

The trained model file (`model.keras`) is not included in this repository. Run `train.py` to train the model before running `generate.py`.

---

## 👩‍💻 Developed By

**Hari Priya**

B.Tech – Artificial Intelligence & Machine Learning

Pragati Engineering College

CodeAlpha Internship Project
