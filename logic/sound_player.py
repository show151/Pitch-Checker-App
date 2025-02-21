import os
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

class SoundPlayer:
  def __init__(self):
    self.player = QMediaPlayer()
    self.audio_output = QAudioOutput()
    self.player.setAudioOutput(self.audio_output)

  def play_sound(self, file_path):
    if not os.path.exists(file_path):
      print("MP3 file dose not exist:", file_path)
      return
    url = QUrl.fromLocalFile(os.path.abspath(file_path))
    self.player.setSource(url)
    self.player.play()