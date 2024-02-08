from enum import Enum
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt, QEvent

class PhotocardState(Enum):
    """ Photocard State enumeration."""

    OWNED = 0
    WANTED = 1
    LIKED = 2

class Photocard(QWidget):
    """ Photocard widget class"""

    def __init__(self, position: tuple, size: tuple, parent) -> None:
        super().__init__()  # Call the inherited classes __init__ method


        self.parent = parent
        self.size = size
        self.position = position

        self.setParent(self.parent.ui)

        self.setGeometry(position[0], position[1], size[0], size[1])
        # print(f"Widget created at {position} of size {size}")

        self.owned: bool = False
        self.liked: bool = False
        self.wanted: bool = False

        self.show()

        # add child widgets

        # --------- TEMPORARY WIDGET ----------
        self.label: QLabel = QLabel(self)
        self.label.setText("HOVER ON")
        self.label.hide()

        self.label_owned: QLabel = QLabel(self)
        self.label_owned.setText("Owned")
        self.label_owned.move(0, 10)
        self.label_owned.hide()

        self.label_liked: QLabel = QLabel(self)
        self.label_liked.setText("liked")
        self.label_liked.move(0, 20)
        self.label_liked.hide()

        self.label_wanted: QLabel = QLabel(self)
        self.label_wanted.setText("Wanted")
        self.label_wanted.move(0, 30)
        self.label_wanted.hide()
        # ------------------------------------

    def event(self, event):
        if event.type() == QEvent.Type.Enter:
            self.on_hover()
        elif event.type() == QEvent.Type.Leave:
            self.out_hover()
        return super().event(event)

    def on_hover(self):
        self.label.show()
    def out_hover(self):
        self.label.hide()

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            match self.parent.mode:
                case PhotocardState.OWNED:
                    self.setup_owned()
                case PhotocardState.WANTED:
                    self.setup_wanted()
                case PhotocardState.LIKED:
                    self.setup_liked()
                case _:
                    self.setup_owned()

    def setup_liked(self):
        if self.liked:
            # hide widget liked
            self.label_liked.hide()

            self.liked = False
        else:
            # show widget liked
            self.label_liked.show()

            self.liked = True

    def setup_owned(self):
        if self.owned:
            # hide widget owned
            self.label_owned.hide()

            self.owned = False
        else:
            # show widget owned
            self.label_owned.show()
            self.owned = True

    def setup_wanted(self):
        if self.wanted:
            # hide widget wanted
            self.label_wanted.hide()
            self.wanted = False
        else:
            # show widget wanted
            self.label_wanted.show()
            self.wanted = True