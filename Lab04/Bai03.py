import sys
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont

class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 48))

        # Thiết lập màu chữ
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor('green'))
        self.label.setPalette(palette)

        self.setCentralWidget(self.label)

        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)  # Cập nhật mỗi giây

        self.updateTime()  # Cập nhật thời gian ban đầu

    def updateTime(self):
        currentTime = QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(currentTime)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())