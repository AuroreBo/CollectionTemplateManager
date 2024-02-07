
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt, QEvent

class Photocard(QWidget):
    """ Photocard widget class"""

    def __init__(self, position: tuple, size: tuple, parent: QWidget) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        # self.widget = QWidget(parent)
        self.setParent(parent)
        self.size = size
        self.position = position

        self.setGeometry(position[0], position[1], size[0], size[1])
        # print(f"Widget created at {position} of size {size}")

        # btn = QPushButton(self.widget)
        # btn.setText("TEST")
        # self.setStyleSheet("background-color:black;")

        self.show()
        self.label: QLabel = QLabel(self)
        self.label.setText("HOVER ON")
        self.label.hide()


    def event(self, event):
        if event.type() == QEvent.Type.Enter:
            self.on_hover()
        elif event.type() == QEvent.Type.Leave:
            self.out_hover()
        return super().event(event)

    def on_hover(self):
        self.label.show()
    def out_hover(self):
        print("out")
        self.label.hide()
