import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menu Example')
        self.setGeometry(100, 100, 400, 300)

        # Tạo menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # Tạo hành động Open
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        # Tạo hành động Save
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        # Tạo hành động Exit
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        self.show()

    def openFile(self):
        QMessageBox.information(self, 'Info', 'Open file menu item selected')

    def saveFile(self):
        QMessageBox.information(self, 'Info', 'Save file menu item selected')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
