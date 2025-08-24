import sys
from pathlib import Path

# To be sure that imports will work
pr = Path(__file__).parent.parent
sys.path.append(str(pr))

from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSizePolicy,
)


class MainWindow(QWidget):
     
    def __init__(self, app_name):
        super().__init__()
        self.setWindowTitle(app_name)
        self._init_ui()

    def _init_ui(self):
        self.mainLayout = QVBoxLayout()

        # --- Button layouts ---
        buttonsLayout = QHBoxLayout()
        buttonsLayout.setContentsMargins(10, 10, 10, 10)
        buttonsLayout.setSpacing(10)

        self.todayButton = QPushButton('Today')
        self.upcomingButton = QPushButton('Upcoming')
        self.anyTimeButton = QPushButton('Anytime')
        self.logBookButton  = QPushButton('Logbook')

        for btn in (self.todayButton, self.upcomingButton, self.anyTimeButton, self.logBookButton):
            btn.setMinimumHeight(40)
            btn.setMinimumWidth(140)

            # How buttons will behave when the window will be resized
            # horizontal behavior :: vertical behavior
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed) 
            btn.setStyleSheet(self._button_style())


    # --- Button styling ---
    @staticmethod
    def _button_style(font_size: int = 16) -> str:
        return f"""
        QPushButton {{
            background-color: #444;
            color: white;
            border: 2px solid #888;
            border-radius: 10px;
            font-size: {font_size}px;
            padding: 10px 16px;
            margin-top: 10px;
        }}
        QPushButton:hover {{
            background-color: #666;
            border: 2px solid #aaa;
        }}
        QPushButton:pressed {{
            background-color: #222;
        }}
        """