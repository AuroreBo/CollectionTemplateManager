
from PyQt6.QtWidgets import (
    QWidget
)

from detection_form import Ui_detection_settings_window


class DetectionSettings:
    # adjust contrast depending on card brightness
    card_type: bool = True
    # allow pixel variation around the average card size
    margin: int = 35
    # clean detection of small item (text, details... )
    minimum_noise: int = 20

# Create the preview view window class
class DetectionSettingsUI(QWidget):
    """Preview View class."""

    def __init__(self) -> None:
        """Init the connecting window."""
        super().__init__()
        self.ui = Ui_detection_settings_window()
        self.ui.setupUi(self)  # type: ignore[no-untyped-call]