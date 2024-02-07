from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QGroupBox,
    QMainWindow,
    QMenu,
    QWidget,
)

from win32api import GetSystemMetrics

from form import Ui_global_form
from template import Template


class TemplateManager(QMainWindow):
    """Main GUI app."""

    def __init__(self, name: str) -> None:
        super().__init__()  # Call the inherited classes __init__ method

        # self.move(0, 0)
        self.app_name = name

        self.ui = Ui_global_form()
        self.ui.setupUi(self)
        self.resize(self.ui.scrollArea.width()+10, self.ui.scrollArea.height()+10)

        self.template: Template = None

        self.ui.select_template_button.clicked.connect(self.select_template)

    def select_template(self):
        filter = "*.png *.jpg"
        img = QFileDialog.getOpenFileName(self, "Select Template", ".", filter)

        if img != ("",""):
            # Update UI
            self.ui.template_path.setText(img[0])

            self.template = Template(img[0], self)

            marge = int(GetSystemMetrics(1) * 0.2)
            self.resize(self.template.width+20, GetSystemMetrics(1)-marge)
            self.move(50,50)
            # self.ui.scrollArea.setWidgetResizable(True)
            # self.ui.scrollArea.resize(self.template.width, self.height())

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.ui.scrollArea.resize(self.width()-10, self.height())




