import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Đặt thuộc tính cho cửa sổ (tiêu đề và kích thước ban đầu)
        self.setWindowTitle("Máy tính cơ bản")
        self.setGeometry(100, 100, 400, 400)  # (x, y, chiều rộng, chiều cao)

        # Tạo widget trung tâm cho cửa sổ chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tạo một QLineEdit widget để nhập và hiển thị kết quả
        self.input_display = QLineEdit()
        self.input_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_display.setReadOnly(True)

        # Tạo layout cho các nút
        button_layout = QVBoxLayout()

        # Tạo các nút số
        number_buttons_layout = QVBoxLayout()
        for i in range(1, 10):
            number_button = QPushButton(str(i))
            number_button.clicked.connect(lambda checked, ch=i: self.on_number_button_click(ch))
            number_buttons_layout.addWidget(number_button)

        # Tạo các nút đặc biệt (0, ., =)
        zero_button = QPushButton("0")
        zero_button.clicked.connect(lambda: self.on_number_button_click(0))

        dot_button = QPushButton(".")
        dot_button.clicked.connect(self.on_dot_button_click)

        equals_button = QPushButton("=")
        equals_button.clicked.connect(self.calculate_result)

        # Tạo các nút toán tử (+, -, *, /)
        operator_buttons_layout = QVBoxLayout()
        operators = ["+", "-", "*", "/"]
        for operator in operators:
            operator_button = QPushButton(operator)
            operator_button.clicked.connect(lambda checked, ch=operator: self.on_operator_button_click(ch))
            operator_buttons_layout.addWidget(operator_button)

        # Tạo layout cho các nút số và các nút đặc biệt
        number_special_buttons_layout = QHBoxLayout()
        number_special_buttons_layout.addLayout(number_buttons_layout)
        number_special_buttons_layout.addWidget(zero_button)
        number_special_buttons_layout.addWidget(dot_button)
        number_special_buttons_layout.addWidget(equals_button)

        # Tạo layout cho tất cả các nút
        button_layout.addLayout(number_special_buttons_layout)
        button_layout.addLayout(operator_buttons_layout)

        # Tạo layout dọc cho toàn bộ máy tính
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_display)
        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

        # Khởi tạo trạng thái máy tính
        self.current_input = ""
        self.operator = ""
        self.operand1 = None

    def on_number_button_click(self, number):
        self.current_input += str(number)
        self.input_display.setText(self.current_input)

    def on_dot_button_click(self):
        if "." not in self.current_input:
            self.current_input += "."
            self.input_display.setText(self.current_input)

    def on_operator_button_click(self, operator):
        if self.current_input:
            if self.operand1 is None:
                self.operand1 = float(self.current_input)
            else:
                self.operand1 = self.calculate(self.operand1, float(self.current_input), self.operator)
            self.operator = operator
            self.current_input = ""
            self.input_display.setText(f"{self.operand1} {operator}")

    def calculate_result(self):
        if self.current_input and self.operand1 is not None:
            result = self.calculate(self.operand1, float(self.current_input), self.operator)
            self.input_display.setText(str(result))
            self.current_input = str(result)
            self.operand1 = None
            self.operator = ""

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 != 0:
                return operand1 / operand2
            else:
                return "Error"

def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
