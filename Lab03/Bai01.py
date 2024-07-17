import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt Button Click Example')
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton('Click me!', self)
        self.button.setGeometry(150, 80, 100, 40)
        self.button.clicked.connect(self.show_message)

        self.show()

    def show_message(self):
        QMessageBox.information(self, 'Message', 'Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

