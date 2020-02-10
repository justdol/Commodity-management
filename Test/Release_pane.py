from PyQt5.Qt import *
from release import Ui_Form


class ReleasePane(QWidget, Ui_Form):
    show_my_pane_singal = pyqtSignal()
    show_index_pane_singal = pyqtSignal()
    add_object_singal = pyqtSignal(str, str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def showIndex(self):
        self.show_index_pane_singal.emit()

    def showMy(self):
        self.show_my_pane_singal.emit()

    def releaseObject(self):
        name = self.Line_name.text()
        price = self.Line_price.text()
        describe = self.Line_describe.text()
        self.add_object_singal.emit(name, price, describe)

    def enable_releasebtn(self):
        describe = self.Line_describe.text()
        price = self.Line_price.text()
        name = self.Line_name.text()
        if len(name) > 0 and len(price) > 0 and len(describe) > 0 :
            self.releasebtn.setEnabled(True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ReleasePane()

    window.show()
    sys.exit(app.exec_())


def show_object():
    objectinfo = objections.getObjectInfo()

    row = len(objectinfo)
    vol = len(objectinfo[0])
    Index_pane.tableWidget.setRowCount(row)
    Index_pane.tableWidget.setColumnCount(vol)
    for i in range(row):
        for z in range(vol):
            temp = objectinfo[i][z]
            data = QTableWidgetItem(str(temp))
            Index_pane.tableWidget.setItem(i, z, data)
