from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QGroupBox,
    QMainWindow,
    QMenu,
    QWidget,
)

from form import Ui_Form
from template import Template


class TemplateManager(QMainWindow):
    """Main GUI app."""

    def __init__(self, name: str = "Template Manager") -> None:
        super().__init__()  # Call the inherited classes __init__ method

        # self.move(0, 0)
        self.app_name = name

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.template: Template = None

        self.ui.select_template_button.clicked.connect(self.select_template)

    def select_template(self):
        filter = "*.png *.jpg"
        img= QFileDialog.getOpenFileName(self, "Select Template", ".", filter)

        # Update UI
        self.ui.template_path.setText(img[0])

        self.template = Template(img[0], self.ui.img_widget)

        print(self.template.width, self.template.height + 100)

        # self.ui.resize(self.template.width, self.template.height + 100)
        # self.ui.img_widget.setStyleSheet("background-image: url("+ img[0] +")")
        # self.ui.img_widget.setStyleSheet("QWidget {background-image: url("+ self.template +") }")





