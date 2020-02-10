from PyQt5.Qt import *
from my import Ui_Form


class MyPane(QWidget, Ui_Form):
    show_release_pane_singal = pyqtSignal()
    show_index_pane_singal = pyqtSignal()
    show_my2_pane_singal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def showIndex(self):
        self.show_index_pane_singal.emit()

    def showRelease(self):
        self.show_release_pane_singal.emit()

    def downObject(self):
        QMessageBox.about(self, "温馨提醒", "该功能尚在开发中,敬请期待")

    def alterObject(self):
        QMessageBox.about(self, "温馨提醒", "该功能尚在开发中,敬请期待")

    def renewObject(self):
        QMessageBox.about(self, "温馨提醒", "该功能尚在开发中,敬请期待")

    def showBuy(self):
        self.show_my2_pane_singal.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyPane()

    window.show()
    sys.exit(app.exec_())
