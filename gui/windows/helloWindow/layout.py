from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,

    QLabel
)

from PySide6.QtCore import Qt

class MainLayout(QHBoxLayout):

    label_hello: QLabel

    def on_create(self):
        self.label_hello = QLabel()
        self.label_hello.setText("Hello World!")
        font = self.label_hello.font()
        font.setPointSize(50)
        self.label_hello.setFont(font)

        self.addWidget(self.label_hello)
        self.setAlignment(Qt.AlignHCenter)  # type: ignore

    def __init__(self):
        super(MainLayout, self).__init__()

        self.on_create()

