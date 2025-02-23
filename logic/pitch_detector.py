import numpy as np

def detect_pitch(audio_data, rate=44100):
  spectrum = np.fft.fft(audio_data)
  freqs = np.fft.fftfreq(len(audio_data), 1 / rate)
  magnitude = np.abs(spectrum)

  positive_freqs = freqs[:len(freqs) // 2]
  positive_magnitude = magnitude[:len(magnitude) // 2]

  peak_index = np.argmax(positive_magnitude)
  fundamental_freq = positive_freqs[peak_index]

  return fundamental_freq
