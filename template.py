import cv2

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QGroupBox,
    QMenu,
    QWidget,
)

class Template(QWidget):
    """ Template widget class"""
    def __init__(self, path: str, ui: QWidget) -> None:
        super().__init__()  # Call the inherited classes __init__ method


        self.path = path

        self.ui = ui


        self.img = cv2.imread(self.path)
        self.width, self.height, _ = self.img.shape
        # self.ui.resize(self.width, self.height)
        self.ui.resize(self.width, 100)
        self.ui.setMaximumWidth(self.width)
        self.ui.setMaximumHeight(self.height)
        self.ui.setStyleSheet("background-image: url(" + self.path + ")")

