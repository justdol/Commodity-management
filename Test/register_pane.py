from PyQt5.Qt import *
from register import Ui_Form


class RegisterPane(QWidget, Ui_Form):
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 允许加载背景图片
        self.setupUi(self)

        self.animation_targets = [self.about_menu_btn, self.reset_menu_btn, self.exit_menu_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

    def show_hid_menue(self, checked):  # check用于检测是否选中

        animation_group = QSequentialAnimationGroup(self)  # 序列动画组
        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()  # 属性动画
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if not checked:
                animation.setStartValue(self.main_menu_btn.pos())
                animation.setEndValue(self.animation_targets_pos[idx])
            else:
                animation.setStartValue(self.animation_targets_pos[idx])
                animation.setEndValue(self.main_menu_btn.pos())
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)  # 弹簧效果
            animation_group.addAnimation(animation)

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def about_wc(self):
        QMessageBox.about(self, "关于", "王驰 1801010083 计科一班")

    def reset(self):
        self.account_lineEdit.clear()
        self.passWord_lineEdit.clear()
        self.conform_passWord_lineEdit.clear()

    def exit_pane(self):
        self.exit_signal.emit()

    def check_register(self):
        account_txt = self.account_lineEdit.text()
        password_txt = self.passWord_lineEdit.text()
        self.register_account_pwd_signal.emit(account_txt, password_txt)

    def enable_registerbtn(self):
        account_txt = self.account_lineEdit.text()
        password_txt = self.passWord_lineEdit.text()
        cp_txt = self.conform_passWord_lineEdit.text()
        if len(account_txt) > 0 and len(password_txt) > 0 and len(cp_txt) > 0 and password_txt == cp_txt:
            self.reguster_pushButton.setEnabled(True)
        else:
            self.reguster_pushButton.setEnabled(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda: print("退出"))
    window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()
    sys.exit(app.exec_())
