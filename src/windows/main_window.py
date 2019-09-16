import PyQt5.QtWidgets as Qw
import PyQt5.QtCore as Qc


class MainWindow(Qw.QMainWindow):
    def __init__(self, mode=None):
        Qw.QMainWindow.__init__(self)
        self.mode = mode
        self.mdiArea = Qw.QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qc.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qc.Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)
        # self.mdiArea.subWindowActivated.connect(self.updateMenus)
