from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


try:
    QApplication.serAttribute(Qt.AA_EnableHighDpiScaling)
except AttributeError:
    pass


def get_app():
    return QApplication.instance()


class TerpApp(QApplication):
    def __init__(self, *args, mode=None):
        QApplication.__init__(self, *args)
        from windows.main_window import MainWindow
        self.window = MainWindow(mode)

    def run(self):
        self.window.show()
        res = self.exec_()
        # put code here
        # ...
        return res
