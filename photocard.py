from enum import Enum
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt, QEvent

from type_widget import WidgetOnLike, WidgetOnOwned, WidgetOnWanted

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

        self.owned: bool = False
        self.liked: bool = False
        self.wanted: bool = False

        self.show()

        # --------- WIDGET FOR EACH MODE ----------
        self.owned_widget = WidgetOnOwned(self)
        self.owned_widget.hide()
        self.owned_widget_hover = WidgetOnOwned(self)
        self.owned_widget_hover.hide()

        self.wanted_widget = WidgetOnWanted(self)
        self.wanted_widget.hide()
        self.wanted_widget_hover = WidgetOnWanted(self)
        self.wanted_widget_hover.hide()

        self.like_widget = WidgetOnLike(self)
        self.like_widget.hide()
        self.like_widget_hover = WidgetOnLike(self)
        self.like_widget_hover.hide()

        # ---------------------------------------

    def event(self, event):
        """ Manage event. """
        if event.type() == QEvent.Type.Enter:
            self.on_hover()
        elif event.type() == QEvent.Type.Leave:
            self.out_hover()
        return super().event(event)

    def on_hover(self) -> None:
        """ Event on hover. """
        match self.parent.mode:
            case PhotocardState.OWNED:
                self.owned_widget_hover.show()
            case PhotocardState.WANTED:
                self.wanted_widget_hover.show()
            case PhotocardState.LIKED:
                self.like_widget_hover.show()
            case _:
                self.owned_widget_hover.show()

    def out_hover(self) -> None:
        """ Event out hover. """
        match self.parent.mode:
            case PhotocardState.OWNED:
                self.owned_widget_hover.hide()
            case PhotocardState.WANTED:
                self.wanted_widget_hover.hide()
            case PhotocardState.LIKED:
                self.like_widget_hover.hide()
            case _:
                self.owned_widget_hover.hide()

    def mousePressEvent(self, event) -> None:
        """ Event on mouse pressed. """
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

    def setup_liked(self) -> None:
        """ Add/Delete liked UI. """
        if self.liked:
            self.parent.liked.remove(self)
            # hide widget liked
            self.like_widget.hide()

            self.liked = False
        else:
            self.parent.liked.append(self)
            # show widget liked
            self.like_widget.show()

            self.liked = True

    def setup_owned(self) -> None:
        """ Add/Delete owned UI. """
        if self.owned:
            self.parent.owned.remove(self)
            # hide widget owned
            self.owned_widget.hide()

            self.owned = False
        else:
            self.parent.owned.append(self)
            # show widget owned
            self.owned_widget.show()

            self.owned = True

    def setup_wanted(self) -> None:
        """ Add/Delete wanted UI. """
        if self.wanted:
            self.parent.wanted.remove(self)
            # hide widget wanted
            self.wanted_widget.hide()

            self.wanted = False
        else:
            self.parent.wanted.append(self)
            # show widget wanted
            self.wanted_widget.show()

            self.wanted = True