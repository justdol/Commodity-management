from PyQt5.Qt import *
from login import Ui_Form


class LoginPane(QWidget, Ui_Form):
    show_regiser_pane_singal = pyqtSignal()
    show_index_pane_singal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def enable_Index(self):
        print('弹出')

    def show_register(self):
        self.show_regiser_pane_singal.emit()

    def Index(self):
        account_txt = self.account_lineEdit.text()
        password_txt = self.passWord_lineEdit.text()
        self.show_index_pane_singal.emit(account_txt, password_txt)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = LoginPane()

    window.show()
    sys.exit(app.exec_())
