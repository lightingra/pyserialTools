import serial
import serial.tools.list_ports

class SerialPort(serial.Serial):

    @classmethod
    def port_list(cls):
        return list(serial.tools.list_ports.comports())

    def __init__(self):
        super(SerialPort, self).__init__()