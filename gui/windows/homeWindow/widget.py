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

from PySide6.QtCore import Slot, Signal

# 添加下拉事件
# clicked
class MyComboBox(QComboBox):
    clicked = Signal()

    def showPopup(self) -> None:
        self.clicked.emit()
        return super().showPopup()

    def __init__(self):
        super(MyComboBox, self).__init__()

import tools.serialport as tools

btn_open: QPushButton
btn_query: QPushButton
combobox_ports: MyComboBox
combobox_baudrate: MyComboBox

txed_receive: QTextEdit

@Slot()
def query_serial_ports():
    global combobox_ports

    combobox_ports.clear()
    ports_list = tools.SerialPort.port_list()
    if len(ports_list) > 0:
        for port in ports_list:
            combobox_ports.addItem(port[0], port[0])

def widget_create():
    global btn_open
    global combobox_ports
    global combobox_baudrate
    global txed_receive
    global txed_send
    
    # btn_open
    btn_open = QPushButton()
    btn_open.setText("open")

    # combobox_baudrate
    combobox_baudrate = MyComboBox()
    combobox_baudrate.addItem("115200", 115200)
    combobox_baudrate.addItem("9600", 9600)

    # combobox_ports
    combobox_ports = MyComboBox()
    combobox_ports.clicked.connect(query_serial_ports)
    
    # txed_receive
    txed_receive = QTextEdit()

    # txed_send
    txed_send = QTextEdit()

    return (
        btn_open,
        combobox_ports,
        combobox_baudrate,

        txed_receive,
        txed_send,
    )
