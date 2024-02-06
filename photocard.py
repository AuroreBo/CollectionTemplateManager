
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
)

class Photocard:
    """ Photocard widget class"""

    def __init__(self, position: tuple, size: tuple, parent: QWidget) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.widget = QWidget(parent)
        self.size = size
        self.position = position

        self.widget.setGeometry(position[0], position[1], size[0], size[1])
        # print(f"Widget created at {position} of size {size}")

        # btn = QPushButton(self.widget)
        # btn.setText("TEST")
        self.widget.setStyleSheet("background-color:black;")

        self.widget.show()


