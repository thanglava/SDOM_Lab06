import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate, Qt

class DateWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Đặt tiêu đề cho cửa sổ
        self.setWindowTitle('Digital Date Widget')

        # Tạo một layout
        layout = QVBoxLayout()

        # Tạo một nhãn để hiển thị ngày
        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignCenter)
        
        # Cập nhật nhãn ngày
        self.update_date()

        # Thêm nhãn vào layout
        layout.addWidget(self.date_label)

        # Đặt layout vào cửa sổ chính
        self.setLayout(layout)

    def update_date(self):
        # Lấy ngày hiện tại
        current_date = QDate.currentDate()

        # Định dạng ngày
        date_string = current_date.toString('dddd-dd/MM/yyyy')

        # Đặt chuỗi ngày vào nhãn
        self.date_label.setText(date_string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    date_widget = DateWidget()
    date_widget.resize(300, 100)
    date_widget.show()
    sys.exit(app.exec_())
