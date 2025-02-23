import pyaudio
import numpy as np

class Recorder:
  def __init__(self, channels=1, rate=44100, frames_per_buffer=1024, record_seconds=2):
    self.channels = channels
    self.rate = rate
    self.frames_per_buffer = frames_per_buffer
    self.record_soconds = record_seconds
    self.audio = pyaudio.PyAudio()

  def record(self):
    stream = self.audio.open(format=pyaudio.paInt16,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             frames_per_buffer=self.frames_per_buffer)

    frames = []

    for _ in range(0, int(self.rate / self.frames_per_buffer * self.record_soconds)):
      data = stream.read(self.frames_per_buffer)
      frames.append(np.frombuffer(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()

    audio_data = np.hstack(frames)
    return audio_data

  def terminate(self):
    self.audio.terminate()
