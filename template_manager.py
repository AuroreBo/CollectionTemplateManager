from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QGroupBox,
    QMainWindow,
    QMenu,
    QWidget,
)

from form import Ui_global_form
from template import Template


class TemplateManager(QMainWindow):
    """Main GUI app."""

    def __init__(self, name: str = "Template Manager") -> None:
        super().__init__()  # Call the inherited classes __init__ method

        # self.move(0, 0)
        self.app_name = name

        self.ui = Ui_global_form()
        self.ui.setupUi(self)

        self.template: Template = None

        self.ui.select_template_button.clicked.connect(self.select_template)

    def select_template(self):
        filter = "*.png *.jpg"
        img= QFileDialog.getOpenFileName(self, "Select Template", ".", filter)

        if img is not None:
            # Update UI
            self.ui.template_path.setText(img[0])

            self.template = Template(img[0], self.ui.img_widget)

            self.resize(self.template.width+20, self.height()+100)
            self.ui.scrollArea.setWidgetResizable(True)
            self.ui.scrollArea.resize(self.template.width, self.height())
            # self.ui.img_widget.setStyleSheet("background-image: url("+ img[0] +")")
            # self.ui.img_widget.setStyleSheet("QWidget {background-image: url("+ self.template +") }")





