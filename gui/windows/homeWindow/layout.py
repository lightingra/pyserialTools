from PySide6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,

    QPushButton,
    QComboBox,
    QTextEdit
)

from PySide6.QtCore import Qt

from .widget import widget_create

class MainLayout(QHBoxLayout):

    layout1: QVBoxLayout
    layout2: QVBoxLayout

    def on_create(self):
        (
        btn_open,
        combobox_ports,
        combobox_baudrate,

        txed_receive,
        txed_send,
            ) = widget_create()

        # layout1
        self.layout1 = QVBoxLayout()

        # layout1 add widget
        self.layout1.addWidget(combobox_ports)
        self.layout1.addWidget(combobox_baudrate)
        self.layout1.addWidget(btn_open)
        self.layout1.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # type: ignore

        # layout2
        self.layout2 = QVBoxLayout()

        # layout2 add widget
        self.layout2.addWidget(txed_receive)
        self.layout2.addWidget(txed_send)
        self.layout2.setStretchFactor(txed_receive, 3)
        self.layout2.setStretchFactor(txed_send, 1)

        # add layouts
        self.addLayout(self.layout1)
        self.addLayout(self.layout2)

    def __init__(self):
        super(MainLayout, self).__init__()

        self.on_create()

