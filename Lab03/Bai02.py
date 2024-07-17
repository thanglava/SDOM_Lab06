import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QLabel

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Character Counter")
    window.setGeometry(100, 100, 400, 200)  # (x, y, width, height)
    layout = QVBoxLayout()
    
    # Tạo một widget QTextEdit để nhập văn bản
    text_edit = QTextEdit(window)
    layout.addWidget(text_edit)
    
    # Tạo một QLabel để hiển thị số lượng ký tự
    char_count_label = QLabel("Character Count: 0", window)
    layout.addWidget(char_count_label)
    
    # Kết nối tín hiệu textChanged của QTextEdit với một slot để cập nhật số lượng ký tự
    def update_char_count():
        char_count = len(text_edit.toPlainText())
        char_count_label.setText(f"Character Count: {char_count}")
    
    text_edit.textChanged.connect(update_char_count)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
