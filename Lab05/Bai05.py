import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QDialog, QPushButton, QLineEdit, QLabel, QSpinBox, QHBoxLayout, QDialogButtonBox, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Custom dialog')
        self.resize(400, 200)  

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.model_dialog_btn = QPushButton('Model dialog')
        self.modeless_dialog_btn = QPushButton('Modeless dialog')
        self.quit_btn = QPushButton('Thoát')

        self.model_dialog_btn.clicked.connect(self.show_model_dialog)
        self.modeless_dialog_btn.clicked.connect(self.show_modeless_dialog)
        self.quit_btn.clicked.connect(self.close)

        button_layout.addWidget(self.model_dialog_btn)
        button_layout.addWidget(self.modeless_dialog_btn)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.quit_btn)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def show_model_dialog(self):
        dialog = CustomDialog(self)
        dialog.exec_()

    def show_modeless_dialog(self):
        self.dialog = CustomDialog(self)
        self.dialog.show()

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Custom Model Dialog')
        self.resize(300, 150) 

        layout = QVBoxLayout()

        name_label = QLabel('Tên:')
        self.name_input = QLineEdit()

        age_label = QLabel('Tuổi:')
        self.age_input = QSpinBox()
        self.age_input.setMaximum(150)

        form_layout = QHBoxLayout()
        form_layout.addWidget(name_label)
        form_layout.addWidget(self.name_input)

        form_layout.addWidget(age_label)
        form_layout.addWidget(self.age_input)

        layout.addLayout(form_layout)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.buttons)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
