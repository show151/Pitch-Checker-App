from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox
from PySide6.QtCore import QTimer, Qt
from logic.sound_player import play_sequence
from logic.recorder import Recorder
from logic.pitch_detector import detect_pitch
from logic.matcher import match_pitch
import config

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("音程練習アプリ")
    self.setFixedSize(600, 400)
    self.setStyleSheet("background-color: #1E2A38; color: #FFFFFF;")

    self.sound_sel = QComboBox(self)
    self.sound_sel.addItems(config.SEQUENCIES.keys())
    self.sound_sel.setStyleSheet("font-size: 18px; padding: 5px;")

    self.label = QLabel("一致率", self)
    self.label.setAlignment(Qt.AlignCenter)
    self.label.setStyleSheet("font-size: 24px;")

    self.result_label = QLabel("", self)
    self.result_label.setAlignment(Qt.AlignCenter)
    self.result_label.setStyleSheet("font-size: 20px;")

    self.play_bt = QPushButton("再生", self)
    self.play_bt.clicked.connect(self.play_and_record)
    self.play_bt.setStyleSheet("""
      background-color: #3498db;
      color: white;
      font-size: 18px;
      border-radius: 10px;
      padding: 10px;
    """)

    layout = QVBoxLayout()
    layout.addWidget(self.label)
    layout.addWidget(self.sound_sel)
    layout.addWidget(self.play_bt)
    layout.addWidget(self.result_label)

    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)

  def play_and_record(self):
    self.result_label.setText("")
    self.play_bt.setEnabled(False)

    selected_sound = self.sound_sel.currentText()
    play_sequence(selected_sound)

    self.countdown = 3
    self.label.setText(str(self.countdown))

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_countdown)
    self.timer.start(1000)

  def update_countdown(self):
    self.countdown -= 1
    if self.countdown > 0:
      self.label.setText(str(self.countdown))
    else:
      self.timer.stop()
      self.label.setText("録音中")
      self.record_audio()

  def record_audio(self):
    recorder = Recorder()
    audio_data = recorder.record()

    detected_pitch = detect_pitch(audio_data)
    selected_sound = self.sound_sel.currentText()
    target_pitches = [config.NOTE_FREQUENCIES[note]
                      for note in config.SEQUENCIES[selected_sound]]
    match_rate = match_pitch(detected_pitch, target_pitches)

    self.result_label.setText(f"一致率: {match_rate}%")

    if match_rate >= 80:
      self.setStyleSheet("background-color: #2ecc71; color: #FFFFFF;")
    else:
      self.setStyleSheet("background-color: #e74c3c; color: #FFFFFF;")

    self.play_bt.setEnabled(True)
