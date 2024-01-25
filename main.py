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


# __________________________________________________
# Variables.
# __________________________________________________
window_width = 500
window_height = 500
# __________________________________________________
# Main.
# __________________________________________________
def main() -> None:

    app = QApplication([])
    app_name = "Template Manager"


    window = QWidget()
    window.setWindowTitle(app_name)
    window.resize(window_width, window_height)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()