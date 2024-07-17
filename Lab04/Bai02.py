import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen, QMouseEvent
from PyQt5.QtCore import Qt, QPoint


class DrawingApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.drawing = False
        self.lastPoint = QPoint()

    def initUI(self):
        self.setWindowTitle('Drawing Application')
        self.setGeometry(100, 100, 600, 400)

        mainMenu = self.menuBar()
        shapeMenu = mainMenu.addMenu('Shapes')

        lineAction = QAction('Line', self)
        lineAction.triggered.connect(self.drawLine)
        shapeMenu.addAction(lineAction)

        rectangleAction = QAction('Rectangle', self)
        rectangleAction.triggered.connect(self.drawRectangle)
        shapeMenu.addAction(rectangleAction)

        triangleAction = QAction('Triangle', self)
        triangleAction.triggered.connect(self.drawTriangle)
        shapeMenu.addAction(triangleAction)

        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)

    def drawLine(self):
        self.canvas.currentShape = 'line'

    def drawRectangle(self):
        self.canvas.currentShape = 'rectangle'

    def drawTriangle(self):
        self.canvas.currentShape = 'triangle'


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.currentShape = None
        self.shapes = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        for shape in self.shapes:
            if shape['type'] == 'line':
                painter.drawLine(shape['start'], shape['end'])
            elif shape['type'] == 'rectangle':
                painter.drawRect(shape['start'].x(), shape['start'].y(),
                                 shape['end'].x() - shape['start'].x(),
                                 shape['end'].y() - shape['start'].y())
            elif shape['type'] == 'triangle':
                points = [
                    shape['start'],
                    QPoint(shape['end'].x(), shape['start'].y()),
                    QPoint((shape['start'].x() + shape['end'].x()) // 2, shape['end'].y())
                ]
                painter.drawPolygon(*points)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.drawing = False
            if self.currentShape:
                self.shapes.append({
                    'type': self.currentShape,
                    'start': self.startPoint,
                    'end': self.endPoint
                })
                self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = DrawingApplication()
    mainWindow.show()
    sys.exit(app.exec_())
2