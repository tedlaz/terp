import platform
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.QtCore import PYQT_VERSION_STR
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSettings


try:
    QApplication.serAttribute(Qt.AA_EnableHighDpiScaling)
except AttributeError:
    pass


def get_app():
    return QApplication.instance()


class TerpApp(QApplication):
    def __init__(self, *args, mode=None):
        QApplication.__init__(self, *args)
        self.mode = mode

        try:
            from classes import info
            from classes.logger import log

            import time

            log.info('=' * 60)
            log.info(time.asctime().center(60))
            log.info('starting new session'.center(60))
        except (ImportError, ModuleNotFoundError) as ex:
            tb = traceback.format_exc()
            QMessageBox.warning(
                None,
                "Import Error",
                "Module: %(name)s\n\n%(tb)s" % {"name": ex.name, "tb": tb}
            )
            # Stop launching and exit
            raise
            sys.exit()
        except Exception:
            raise
            sys.exit()

        try:
            log.info('-' * 60)
            log.info(f'terp version: {info.VERSION}')
            log.info(f'os: {platform.platform()}')
            log.info(f'processor: {platform.processor()}')
            log.info(f'machine: {platform.machine()}')
            log.info(f'python version: {platform.python_version()}')
            log.info(f'qt5 version: {QT_VERSION_STR}')
            log.info(f'pyqt5 version: {PYQT_VERSION_STR}')
        except Exception:
            pass

        self.aboutToQuit.connect(self.onLogTheEnd)

    def run(self, minfo):
        self.setOrganizationName(minfo.COMPANY_NAME)
        self.setOrganizationDomain(minfo.ORG_DOMAIN)
        self.setApplicationName(minfo.NAME)
        self.settings = QSettings()
        from windows.main_window import MainWindow
        self.window = MainWindow(self.mode)
        self.window.show()
        res = self.exec_()
        # put code here
        # ...
        return res

    @pyqtSlot()
    def onLogTheEnd(self):
        """ Log when the primary Qt event loop ends """
        try:
            from classes.logger import log
            import time
            log.info('-' * 60)
            log.info('terp\'s session ended'.center(60))
            log.info(time.asctime().center(60))
            log.info('=' * 60)
        except Exception:
            pass

        # return 0 on success
        return 0
