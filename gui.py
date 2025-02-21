from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont, QPalette, QColor
from logic.sound_player import SoundPlayer

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Pitch Checker App")
    self.resize(800, 600)
    self.init_ui()
    self.sound_player = SoundPlayer()

  def init_ui(self):
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#1E1E2F"))
    palette.setColor(QPalette.Button, QColor("#3A7BD5"))
    palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
    self.setPalette(palette)

    layout = QVBoxLayout()

    self.info_label = QLabel("正解音を再生します")
    self.info_label.setFont(QFont("Arial", 16))
    self.info_label.setStyleSheet("color: white;")
    layout.addWidget(self.info_label)

    self.play_button = QPushButton("正解音再生")
    self.play_button.setFont(QFont("Arial", 14))
    self.play_button.setStyleSheet("""
      QPushButton {
        background-color: #3A7BD5;
        color: white;
        border-radius: 10px;
        padding: 10px;
      }
      QPushButton:hover {
        background-color: #5AA9F1;
      }
    """)
    self.play_button.clicked.connect(self.play_reference_sound)
    layout.addWidget(self.play_button)

    self.setLayout(layout)

  def play_reference_sound(self):
    mp3_path = ""
    self.sound_player.play_sound(mp3_path)
