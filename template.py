import cv2
import os
from pathlib import Path
import numpy as np
from PIL import Image

from photocard import Photocard, PhotocardState
from draw_utils import draw_liked, draw_owned, draw_wanted

from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QPixmap, QImageReader, QImage
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QGroupBox,
    QMenu,
    QLabel,
    QWidget,
)

class Template(QWidget):
    """ Template widget class"""
    def __init__(self, path: str, window: QMainWindow) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.path = path

        self.window = window
        self.ui = self.window.ui.img_widget
        self.debug_detection_contour: bool = False
        self.photocards: [Photocard] = []
        self.liked: [Photocard] = []
        self.owned: [Photocard] = []
        self.wanted: [Photocard] = []

        self.mode: PhotocardState = PhotocardState.OWNED
        self.window.ui.mode_comboBox.setCurrentText("Owned")

        self.window.ui.debug_checkBox.stateChanged.connect(self.update_debug_button)
        self.window.ui.resize_button.clicked.connect(self.save_resized_image)
        self.window.ui.detect_button.clicked.connect(self.detect_pc)
        self.window.ui.export_button.clicked.connect(self.export_template)
        self.window.ui.debug_checkBox.stateChanged.connect(self.update_debug_button)
        self.window.ui.mode_comboBox.currentTextChanged.connect(self.update_mode)

        self.img = cv2.imread(self.path)
        self.height, self.width, _ = self.img.shape
        self.ui.resize(self.height, self.width)
        self.ui.setMinimumSize(self.width-20, self.height)
        self.ui.setMaximumWidth(self.width)

        self.ui.setStyleSheet("QWidget#img_widget{background-image: url(" + self.path + "); border:0px}")

        self.detect_pc()

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
            self.ui.setStyleSheet("QWidget#img_widget{background-image: url(" + self.path + "); border:0px}")
        else:
            write_status = cv2.imwrite(file_path,self.img)
            if write_status:
                self.ui.setStyleSheet("QWidget#img_widget{background-image: url(" + self.path + "); border:0px}")

    # https://dontrepeatyourself.org/post/edge-and-contour-detection-with-opencv-and-python/
    def detect_pc(self):
        self.clear_pc_widget()
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gamma = 0.2  # change the value here to get different result
        adjusted = self.adjust_gamma(gray, gamma=gamma)
        blurred = cv2.GaussianBlur(adjusted, (3, 3), 0)
        edged = cv2.Canny(blurred, 10, 100)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        dilate = cv2.dilate(edged, kernel, iterations=1)
        contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        image_copy = img.copy()
        image_pc = img.copy()
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

            cv2.drawContours(image_copy, [approx], -1, (0, 0, 255), 5)

            x, y, w, h = cv2.boundingRect(cnt)
            # to clean with average pc width and height
            if w > 70 and w < 85:
                if h > 105 and h < 135:
                    cv2.rectangle(image_pc, (x, y), (x + w, y + h), (36, 255, 12), 8)

                    self.add_pc_widget((x,y),(w,h))

            if self.debug_detection_contour:
                cv2.putText(image_pc, str(w), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                cv2.putText(image_pc, str(h), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        if self.debug_detection_contour:
            image_contours = img.copy()
            # draw the contours on a copy of the original image
            cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
            print(len(contours), "objects were found in this image.")

            # cv2.imshow("Adjusted", adjusted)
            # cv2.imshow("Edged", edged)
            # cv2.imshow("Dilated image", dilate)
            cv2.imshow("contours", image_contours)

            cv2.imshow('copy', image_copy)
            cv2.imshow('pc', image_pc)
        print(self.photocards)
        print(len(self.photocards))

    def add_pc_widget(self, position: tuple, size: tuple):
        pc = Photocard(position, size, self)
        self.photocards.append(pc)

    def clear_pc_widget(self):
        for child in self.ui.children():
            child.deleteLater()

        self.photocards.clear()

    def update_debug_button(self) -> None:
        self.debug_detection_contour = self.window.ui.debug_checkBox.isChecked()

    def update_mode(self) -> None:
        if self.window.ui.mode_comboBox.currentText() == "Owned":
            self.mode = PhotocardState.OWNED
        if self.window.ui.mode_comboBox.currentText() == "Wanted":
            self.mode = PhotocardState.WANTED
        if self.window.ui.mode_comboBox.currentText() == "Favorite":
            self.mode = PhotocardState.LIKED

    def export_template(self) -> None:
        path = QFileDialog.getSaveFileName(self.ui, "Save template location", "", "*.png")
        if path:
            image = Image.open(self.path)
            saving_path = str(path[0])

            #  Process Owned
            image = draw_owned(image, self.owned)
             #  Process Wanted
            image = draw_wanted(image, self.wanted)
            #  Process Liked
            image = draw_liked(image, self.liked)

            #  Save template
            image.save(saving_path, quality=95)


    # ----------------------------------------------------------------------------------------------
    # UTILITIES
    # ----------------------------------------------------------------------------------------------

    # https://stackoverflow.com/questions/33322488/how-to-change-image-illumination-in-opencv-python
    def adjust_gamma(self, image, gamma=1.0):

        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        return cv2.LUT(image, table)

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

