from PySide6.QtWidgets import (
    QMainWindow,
    QWidget
)

from .layout import MainLayout

class MainWindow(QMainWindow):
    mainLayout: MainLayout

    def on_create(self):
        self.resize(640, 480)
        self.setWindowTitle("Hello Window")

    def __init__(self):
        super(MainWindow, self).__init__()

        self.on_create()

        # layout
        self.mainLayout = MainLayout()

        # widget
        widget = QWidget()
        widget.setLayout(self.mainLayout)
        self.setCentralWidget(widget)
        