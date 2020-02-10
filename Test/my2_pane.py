from PyQt5.Qt import *
from my2 import Ui_Form


class My2Pane(QWidget, Ui_Form):
    show_release_pane_singal = pyqtSignal()
    show_index_pane_singal = pyqtSignal()
    show_upmy_pane_singal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def showIndex(self):
        self.show_index_pane_singal.emit()

    def showRelease(self):
        self.show_release_pane_singal.emit()

    def showUp(self):
        self.show_upmy_pane_singal.emit()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = My2Pane()

    window.show()
    sys.exit(app.exec_())
