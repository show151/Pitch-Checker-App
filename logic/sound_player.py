import pyaudio
import wave

def play_sequence(file_path):
  wf = wave.open(file_path, 'rb')

  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paInt16,
                  channels=wf.getnchannels(),
                  rate=wf.getframerate(),
                  output=True)

  data = wf.readframes(1024)
  while data:
    stream.write(data)
    data = wf.readframes(1024)

  stream.stop_stream()
  stream.close()
  p.terminate()
