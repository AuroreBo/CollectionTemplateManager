import cv2
import os
from pathlib import Path
import numpy as np

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
    def __init__(self, path: str, ui: QWidget, window: QMainWindow) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        self.path = path

        self.window = window
        self.ui = ui
        self.debug_detection_contour: bool = False
        self.window.ui.debug_checkBox.stateChanged.connect(self.update_debug_button)
        self.window.ui.resize_button.clicked.connect(self.save_resized_image)
        self.window.ui.detect_button.clicked.connect(self.detect_pc)
        self.window.ui.debug_checkBox.stateChanged.connect(self.update_debug_button)

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

    # https://dontrepeatyourself.org/post/edge-and-contour-detection-with-opencv-and-python/
    def detect_pc(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gamma = 0.2  # change the value here to get different result
        adjusted = self.adjust_gamma(gray, gamma=gamma)
        blurred = cv2.GaussianBlur(adjusted, (3, 3), 0)
        edged = cv2.Canny(blurred, 10, 100)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        dilate = cv2.dilate(edged, kernel, iterations=1)
        contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if self.debug_detection_contour:
            image_copy = img.copy()
            # draw the contours on a copy of the original image
            cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
            print(len(contours), "objects were found in this image.")

            cv2.imshow("Adjusted", adjusted)
            cv2.imshow("Edged", edged)
            # cv2.imshow("Dilated image", dilate)
            cv2.imshow("contours", image_copy)

        font = cv2.FONT_HERSHEY_COMPLEX
        image_copy = img.copy()
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

            # cv2.drawContours(dilate, contours, -1, (0, 0, 255), 5)
            cv2.drawContours(image_copy, [approx], -1, (0, 0, 255), 5)

            # Used to flatted the array containing
            # the co-ordinates of the vertices.
            n = approx.ravel()
            i = 0

            for j in n:
                if (i % 2 == 0):
                    x = n[i]
                    y = n[i + 1]

                    # String containing the co-ordinates.
                    string = str(x) + " " + str(y)

                    if (i == 0):
                        # text on topmost co-ordinate.
                        cv2.putText(dilate, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))
                    else:
                        # text on remaining co-ordinates.
                        cv2.putText(dilate, string, (x, y),font, 0.5, (0, 255, 0))
                i = i + 1


        cv2.imshow('copy', image_copy)

    # https://stackoverflow.com/questions/33322488/how-to-change-image-illumination-in-opencv-python
    def adjust_gamma(self, image, gamma=1.0):

        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        return cv2.LUT(image, table)

    def update_debug_button(self) -> None:
        self.debug_detection_contour = self.window.ui.debug_checkBox.isChecked()

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

