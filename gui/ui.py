from multiprocessing import Process
from PySide6.QtWidgets import QApplication

from PySide6.QtCore import QTimer

from .windows import helloWindow, homeWindow

def service():
    app = QApplication([])

    # windows
    helloWin = helloWindow.MainWindow()
    helloWin.show()

    homeWin = homeWindow.MainWindow()
    timer = QTimer()
    def shot():
        helloWin.close()
        homeWin.show()
    timer.singleShot(1000, shot)

    app.exec() 

app_process: Process

def start_service():
    global app_process

    app_process = Process(target=service)
    app_process.daemon = True
    app_process.start()
    return app_process

def stop_service():
    global app_process
    
    if app_process:
        app_process.join()
