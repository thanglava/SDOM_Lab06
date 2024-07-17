import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Burning widget")
        self.setGeometry(100, 100, 800, 400)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 50, 700, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(675)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.update_graphics)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(50, 100, 700, 100)

        self.rects = []
        for i in range(9):
            rect = QGraphicsRectItem(0, 0, 75, 100)
            rect.setBrush(QColor(255, 255, 204))
            rect.setPen(Qt.NoPen)
            rect.setPos(i * 75, 0)
            self.rects.append(rect)
            self.scene.addItem(rect)

        self.update_graphics(0)

    def update_graphics(self, value):
        for i, rect in enumerate(self.rects):
            if value > i * 75 + 75:
                rect.setBrush(QColor(211, 211, 211))
            else:
                rect.setBrush(QColor(255, 255, 204))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())