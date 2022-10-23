from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel
)

from .layout import MainLayout

class MainWindow(QMainWindow):
    mainLayout: MainLayout

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(640, 480)
        self.setWindowTitle("Home Window")

        # layout
        self.mainLayout = MainLayout()

        # widget
        widget = QWidget()
        widget.setLayout(self.mainLayout)
        self.setCentralWidget(widget)
        