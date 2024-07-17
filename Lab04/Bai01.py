import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MouseEventDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mouse Event Example')
        self.setGeometry(200, 100, 400, 300)

        self.label = QLabel('Mouse Events:', self)
        self.label.setAlignment(Qt.AlignTop)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText(f'Mouse Events: Left Button Pressed at ({event.x()}, {event.y()})')
        elif event.button() == Qt.RightButton:
            self.label.setText(f'Mouse Events: Right Button Pressed at ({event.x()}, {event.y()})')
        elif event.button() == Qt.MiddleButton:
            self.label.setText(f'Mouse Events: Middle Button Pressed at ({event.x()}, {event.y()})')

    def mouseMoveEvent(self, event):
        self.label.setText(f'Mouse Events: Mouse Moved to ({event.x()}, {event.y()})')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MouseEventDemo()
    demo.show()
    sys.exit(app.exec_())
