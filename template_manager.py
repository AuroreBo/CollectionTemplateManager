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
from detection_settings import DetectionSettings, DetectionSettingsUI

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
        self.detection_settings: DetectionSettings = DetectionSettings()
        self.detection_settings_ui: DetectionSettingsUI = DetectionSettingsUI()

        # Init detection settings UI
        self.detection_settings_ui.ui.card_type_checkBox.setChecked(self.detection_settings.card_type)
        self.detection_settings_ui.ui.margin_lineEdit.setText(str(self.detection_settings.margin))
        self.detection_settings_ui.ui.min_noise_lineEdit.setText(str(self.detection_settings.minimum_noise))

        self.ui.select_template_button.clicked.connect(self.select_template)
        self.ui.open_settings_button.clicked.connect(self.open_settings)
        self.detection_settings_ui.ui.card_type_checkBox.stateChanged.connect(self.update_card_type)
        self.detection_settings_ui.ui.margin_lineEdit.textChanged.connect(self.update_margin)
        self.detection_settings_ui.ui.min_noise_lineEdit.textChanged.connect(self.update_min_noise)
        self.detection_settings_ui.ui.detect_preview_button.clicked.connect(self.show_detection_preview)
        self.detection_settings_ui.ui.done_button.clicked.connect(self.close_settings)

    def select_template(self) -> None:
        """ Select template to import. """
        if self.template:
            self.template.deleteLater()

        filter = "*.png *.jpg"
        img = QFileDialog.getOpenFileName(self, "Select Template", ".", filter)

        if img != ("",""):
            # Update UI
            self.ui.template_path.setText(img[0])

            self.template = Template(img[0], self, self.detection_settings)

            marge = int(GetSystemMetrics(1) * 0.2)
            if self.template.height > GetSystemMetrics(1):
                h = GetSystemMetrics(1) - marge
            else:
                h = self.template.height + 50

            self.resize(self.template.width + 20, h)
            self.move(50,50)
            # self.ui.scrollArea.setWidgetResizable(True)
            # self.ui.scrollArea.resize(self.template.width, self.height())

    def resizeEvent(self, event) -> None:
        """ Event when the window is resized. """
        QMainWindow.resizeEvent(self, event)
        self.ui.scrollArea.resize(self.width()-10, self.height())

    def open_settings(self) -> None:
        """ Open settings window. """
        self.detection_settings_ui.show()

    def update_card_type(self) -> None:
        """ Update self.detection_settings.card_type state. """
        self.detection_settings.card_type = self.detection_settings_ui.ui.card_type_checkBox.isChecked()

    def update_margin(self) -> None:
        """ Update self.detection_settings.margin state. """
        if self.detection_settings_ui.ui.margin_lineEdit.text():
            self.detection_settings.margin = int(self.detection_settings_ui.ui.margin_lineEdit.text())

    def update_min_noise(self) -> None:
        """ Update self.detection_settings.minimum_noise state. """
        if self.detection_settings_ui.ui.min_noise_lineEdit.text():
            self.detection_settings.minimum_noise = int(self.detection_settings_ui.ui.min_noise_lineEdit.text())

    def show_detection_preview(self) -> None:
        if self.template:
            self.template.debug_detection_contour = True
            self.template.detect()

    def close_settings(self) -> None:
        self.detection_settings_ui.close()