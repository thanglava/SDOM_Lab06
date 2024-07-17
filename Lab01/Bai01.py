# HoTen:    Nguyễn Hữu Thắng
# MSSV:     2100006065

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def main():
    # Create a PyQt application
    app = QApplication(sys.argv)
    
    # Create a QMainWindow (main window)
    main_window = QMainWindow()
    
    # Set the window properties (title and initial size)
    main_window.setWindowTitle("Blank Window using PyQt")
    main_window.setGeometry(100, 100, 400, 300)  # (x, y, width, height)
    
    # Show the window
    main_window.show()
    
    # Run the application's event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()