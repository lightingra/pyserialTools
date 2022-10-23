import backend.web as backend
import gui.ui as gui

if __name__ == '__main__':
    backend.start_service()
    gui.start_service()

    # 
    gui.stop_service()
    # 
    # backend.stop_service()
    