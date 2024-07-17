# HoTen:    Nguyễn Hữu Thắng
# MSSV:     2100006065

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog, QFontDialog

class WidgetPropertiesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Widget Properties")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QPushButton
        self.button = QPushButton("Click to Customize!")

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add the QPushButton to the layout
        layout.addWidget(self.button)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Connect button click events to customization methods
        self.button.clicked.connect(self.customize_color)
        self.button.clicked.connect(self.customize_font)

    def customize_color(self):
        # Allow the user to select a custom color for the button
        color_dialog = QColorDialog.getColor()
        if color_dialog.isValid():
            self.button.setStyleSheet(f"background-color: {color_dialog.name()};")

    def customize_font(self):
        # Allow the user to select a custom font for the button text
        font_dialog, ok = QFontDialog.getFont()
        if ok:
            self.button.setFont(font_dialog)

def main():
    # Create a PyQt application
    app = QApplication(sys.argv)
    window = WidgetPropertiesApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()