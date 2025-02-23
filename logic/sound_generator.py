import numpy as np
import wave

sample_rate = 44100
note_duration = 0.5
amplitude = 0.5

note_frequencies = {
    "ド↓": 261.63,
    "レ": 293.66,
    "ミ": 329.63,
    "ファ": 349.23,
    "ソ": 392.00,
    "ラ": 440.00,
    "シ": 493.88,
    "ド↑": 523.25,
}

sequences = {
    'ドレド': ['ド↓', 'レ', 'ド↓'],
    'レミレ': ['レ', 'ミ', 'レ'],
    'ミファミ': ['ミ', 'ファ', 'ミ'],
    'ファソファ': ['ファ', 'ソ', 'ファ'],
    'ソラソ': ['ソ', 'ラ', 'ソ'],
    'ラシラ': ['ラ', 'シ', 'ラ'],
    'シドシ': ['シ', 'ド↑', 'シ']
}

def generate_tone(frequency, duration, sample_rate):
  t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
  tone = amplitude * np.sin(2 * np.pi * frequency * t)
  return tone

def save_wave(file_name, data, sample_rate):
  data_int16 = np.int16(data * 32767)
  with wave.open(file_name, 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(data_int16.tobytes())

def generate_and_save_sequences():
  for seq_name, notes in sequences.items():
    tone_list = []
    for note in notes:
      freq = note_frequencies[note]
      tone = generate_tone(freq, note_duration, sample_rate)
      tone_list.append(tone)

    full_sequence = np.concatenate(tone_list)

    file_name = f"sounds/{seq_name}.wav"
    save_wave(file_name, full_sequence, sample_rate)
    print(f"Saved {file_name}")
