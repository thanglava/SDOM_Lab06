import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class FrameRecorder(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: pink;")
        self.setWindowTitle('Frame Recorder')

        title = QLabel('Frame Recorder', self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px;")

        fps_label = QLabel('fps video', self)
        self.fps_input = QLineEdit(self)
        self.fps_input.setPlaceholderText('Enter FPS')
        self.fps_input.setStyleSheet("background-color: white;")


        fps_layout = QHBoxLayout()
        fps_layout.addStretch(1)
        fps_layout.addWidget(QLabel('create an'))
        fps_layout.addWidget(self.fps_input)
        fps_layout.addWidget(fps_label)
        fps_layout.addStretch(1)

        self.pause_button = QPushButton('Pause', self)
        self.start_button = QPushButton('Start', self)
        self.end_button = QPushButton('End', self)

        self.pause_button.setStyleSheet("background-color: yellow; font-size: 16px;")
        self.start_button.setStyleSheet("background-color: green; color: white; font-size: 16px;")
        self.end_button.setStyleSheet("background-color: red; color: white; font-size: 16px;")

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch(1)
        buttons_layout.addWidget(self.pause_button)
        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.end_button)
        buttons_layout.addStretch(1)

        self.status_label = QLabel('Recording Paused', self)
        self.status_label.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addLayout(fps_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

        self.pause_button.clicked.connect(self.pauseRecording)
        self.start_button.clicked.connect(self.startRecording)
        self.end_button.clicked.connect(self.endRecording)

    def pauseRecording(self):
        self.status_label.setText('Recording Paused')

    def startRecording(self):
        self.status_label.setText('Recording Started')

    def endRecording(self):
        self.status_label.setText('Recording Ended')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FrameRecorder()
    ex.show()
    sys.exit(app.exec_())
