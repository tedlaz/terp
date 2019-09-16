import PyQt5.QtWidgets as Qw
import PyQt5.QtCore as Qc
import PyQt5.QtGui as Qg
from classes import info
from resources import terp_rc
from classes.app import get_app


class MainWindow(Qw.QMainWindow):
    def __init__(self, mode=None):
        Qw.QMainWindow.__init__(self)
        self.app = get_app()
        self.mode = mode
        self.mdiArea = Qw.QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qc.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qc.Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)
        # self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.create_actions()
        self.create_menus()
        self.create_toolbars()
        self.statusBar().showMessage("")  # Απαραίτητο για να ενεργοποιηθεί
        self.setWindowIcon(Qg.QIcon(':/images/terp.svg'))

    def create_actions(self):
        self.action_new = Qw.QAction(
            Qg.QIcon(":/images/terp.png"),
            "&Nέο", self, statusTip='Nέο αρχείο',
            triggered=self.trg_new
        )
        self.action_open = Qw.QAction(
            "Άνοιξε", self, statusTip='Άνοιγμα αρχείου',
            triggered=self.trg_open
        )

    def create_menus(self):
        self.menu_file = self.menuBar().addMenu('&Aρχεία')
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)

    def create_toolbars(self):
        self.toolbar_file = self.addToolBar('File')
        self.toolbar_file.addAction(self.action_new)

    def trg_open(self):
        oldfnam = self.app.settings.value("filename", defaultValue=None)
        fnam, _ = Qw.QFileDialog.getOpenFileName(self, 'Open', oldfnam, '')
        if fnam:
            self.app.settings.setValue("filename", fnam)

    def trg_new(self):
        Qw.QMessageBox.information(self, 'new', "not ready yet :-(")
