
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
)
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QPainter


class WidgetOnLike(QWidget):
    """ Liked widget class. """
    def __init__(self, parent: QWidget) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.parent = parent
        self.setParent(self.parent)

    def paintEvent(self, event) -> None:
        """ Draw liked UI. """
        painter = QPainter(self)
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0, 0))
        br = QtGui.QBrush(QtGui.QColor(237, 162, 192, 255))
        painter.setBrush(br)
        painter.setPen(pen)
        painter.drawEllipse(self.parent.size[0]-20, self.parent.size[1]-20, 15, 15)

class WidgetOnOwned(QWidget):
    """ Owned widget class. """
    def __init__(self, parent: QWidget) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.parent = parent
        self.setParent(self.parent)

    def paintEvent(self, event) -> None:
        """ Draw owned UI. """
        painter = QPainter(self)
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0, 0))
        br = QtGui.QBrush(QtGui.QColor(255, 255, 255, 204))
        painter.setPen(pen)
        painter.setBrush(br)
        painter.drawRect(0, 0, self.parent.size[0], self.parent.size[1])

class WidgetOnWanted(QWidget):
    """ Wanted widget class. """
    def __init__(self, parent: QWidget) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.parent = parent
        self.setParent(self.parent)

    def paintEvent(self, event) -> None:
        """ Draw wanted UI. """
        painter = QPainter(self)
        pen = QtGui.QPen(QtGui.QColor(116, 79, 198, 255))
        pen.setWidth(12)
        br = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        painter.setPen(pen)
        painter.setBrush(br)
        painter.drawRect(0, 0, self.parent.size[0], self.parent.size[1])