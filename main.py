import os
import sys
from PySide6.QtWidgets import QApplication
from logic.sound_generator import generate_and_save_sequences
from gui import MainWindow
import config

def check_and_generate_sounds():
  sounds_dir = "sounds"
  os.makedirs(sounds_dir, exist_ok=True)

  for seq_name in config.SEQUENCIES.keys():
    file_path = f"{sounds_dir}/{seq_name}.wav"
    if not os.path.exists(file_path):
      print(f"{file_path}が見つかりません。生成を開始します。")
      generate_and_save_sequences()
      break

def main():
  check_and_generate_sounds()

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()
