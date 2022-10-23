import sys
import os
import PySide6

# fix bug
# qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
if sys.platform == 'win32':
    dirname = os.path.dirname(PySide6.__file__) 
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

import backend.web as backend
import gui.ui as gui

if __name__ == '__main__':
    backend.start_service()
    gui.start_service()

    # 
    gui.stop_service()
    # 
    # backend.stop_service()
    