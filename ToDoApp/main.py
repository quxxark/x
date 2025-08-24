import sys
from PyQt6.QtWidgets import QApplication, QWidget

from ui.main_widget import MainWindow


app_name = "TO-DO APP"


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(app_name)
    window.show()

    sys.exit(app.exec())