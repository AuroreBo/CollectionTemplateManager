import cv2
import os
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QGroupBox,
    QMenu,
    QWidget,
)

class Template(QWidget):
    """ Template widget class"""
    def __init__(self, path: str, ui: QWidget, window :QMainWindow) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.path = path

        self.window = window
        self.ui = ui

        self.img = cv2.imread(self.path)
        self.height, self.width, _ = self.img.shape
        self.ui.resize(self.height, self.width)
        self.ui.setMinimumSize(self.width-20, self.height)
        self.ui.setMaximumWidth(self.width)

        self.ui.setStyleSheet("background-image: url(" + self.path + ")")

    def save_resized_image(self):
        folder_path = Path(self.path).parent.absolute()
        name = Path(self.path).stem

        self.img = self.image_resize(self.img, width=1150)
        self.height, self.width, _ = self.img.shape
        self.ui.resize(self.height, self.width)
        self.ui.setMinimumSize(self.width - 20, self.height)
        self.ui.setMaximumWidth(self.width)
        self.window.resize(self.width,self.window.height())

        # save the new size img
        file_name = name+"_resized.png"
        file_path = str(Path(self.path).parent.absolute())+"/"+file_name
        path = file_path.replace(os.sep, '/')
        self.path = path

        if os.path.exists(file_path):
            self.ui.setStyleSheet("background-image: url(" + self.path + ")")
        else:
            write_status = cv2.imwrite(file_path,self.img)
            if write_status:
                self.ui.setStyleSheet("background-image: url(" + self.path + ")")

    # https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
    def image_resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation=inter)

        # return the resized image
        return resized

