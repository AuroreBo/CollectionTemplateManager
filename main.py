# __________________________________________________
# Librairies includes.
# __________________________________________________

# _____ Utilities _____
from PIL import Image
from io import BytesIO
import numpy as np
import urllib

# _____ UI includes _____
from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget

from PyQt6 import QtCore
from template_manager import TemplateManager

# __________________________________________________
# Variables.
# __________________________________________________
window_width = 580
window_height = 200
# __________________________________________________
# Main.
# __________________________________________________
def main() -> None:

    app = QApplication([])
    app_name = "Template Manager"

    with open("style/Gravira.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = TemplateManager(app_name)

    window.show()
    app.exec()

if __name__ == "__main__":
    main()