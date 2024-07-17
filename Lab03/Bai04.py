import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QShortcut

class ShortcutApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shortcut Example")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)
        
        # Tạo một label để hiển thị thông báo
        self.message_label = QLabel("Press Ctrl+M to show a message", self)
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(self.message_label)
        
        # Tạo một phím tắt Ctrl+M
        shortcut = QKeySequence(Qt.CTRL + Qt.Key_M)
        self.shortcut = QShortcut(shortcut, self)
        self.shortcut.activated.connect(self.show_message)
    
    def show_message(self):
        # Hiển thị thông báo khi phím tắt được kích hoạt
        self.message_label.setText("You pressed Ctrl+M!")

def main():
    app = QApplication(sys.argv)
    window = ShortcutApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
