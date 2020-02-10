from PyQt5.Qt import *
from index import Ui_widget


class IndexPane(QWidget, Ui_widget):
    show_release_pane_singal = pyqtSignal()
    show_my_pane_singal = pyqtSignal()
    search_btn_singal = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def show_my(self):
        self.show_my_pane_singal.emit()

    def show_release(self):
        self.show_release_pane_singal.emit()

    def search_object(self):
        object_name = self.lineEdit.text()
        self.search_btn_singal.emit(object_name)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = IndexPane()

    window.show()
    sys.exit(app.exec_())
