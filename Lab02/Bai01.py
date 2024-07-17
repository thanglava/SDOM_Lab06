import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget

class UngDungCoKhong(QMainWindow):
    def __init__(self):
        super().__init__()

        # Đặt thuộc tính cho cửa sổ (tiêu đề và kích thước ban đầu)
        self.setWindowTitle("Widget Nút Bấm (Có hay Không?)")
        self.setGeometry(100, 100, 400, 200)  # (x, y, chiều rộng, chiều cao)

        # Tạo widget trung tâm cho cửa sổ chính
        widget_trung_tam = QWidget(self)
        self.setCentralWidget(widget_trung_tam)

        # Tạo các nút QPushButton cho "Có" và "Không"
        nut_co = QPushButton("Có")
        nut_khong = QPushButton("Không")

        # Kết nối sự kiện nhấp nút với các phương thức tương ứng
        nut_co.clicked.connect(self.hien_thong_bao_co)
        nut_khong.clicked.connect(self.hien_thong_bao_khong)

        # Tạo layout cho widget trung tâm và thêm các nút vào layout
        bo_cuc = QVBoxLayout()
        bo_cuc.addWidget(nut_co)
        bo_cuc.addWidget(nut_khong)

        # Đặt layout cho widget trung tâm
        widget_trung_tam.setLayout(bo_cuc)

    def hien_thong_bao_co(self):
        QMessageBox.information(self, "Lựa chọn", "Bạn đã chọn: Có")

    def hien_thong_bao_khong(self):
        QMessageBox.information(self, "Lựa chọn", "Bạn đã chọn: Không")

def main():
    app = QApplication(sys.argv)
    cua_so = UngDungCoKhong()
    cua_so.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()