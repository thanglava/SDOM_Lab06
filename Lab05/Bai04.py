import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Input dialog'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        layout = QVBoxLayout()

        # Tạo layout cho hàng đầu tiên
        hbox1 = QHBoxLayout()
        self.label = QLabel('Dialog', self)
        hbox1.addWidget(self.label)

        self.nameLabel = QLabel('Erriez', self)
        hbox1.addWidget(self.nameLabel)
        
        layout.addLayout(hbox1)
        
        # Tạo button
        self.button = QPushButton('Thay đổi tên', self)
        self.button.clicked.connect(self.showDialog)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        
        if ok:
            self.nameLabel.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
