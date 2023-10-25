import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from GUI import Ui_Dialog
from control import Menu, input_queue


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setFixedSize(900, 650)
        self.setWindowTitle("基于机器学习的恶意流量检测系统")

        self.print_thread = Menu()                                           # 开启主进程
        self.print_thread.textbox1.connect(self.update_output_text_1)        # 实现信号与函数槽的连接
        self.print_thread.textbox2.connect(self.update_output_text_2)        # 实现信号与函数槽的连接
        self.ui.pushButton_4.clicked.connect(self.print_thread.start)        # 实现按钮信号与函数槽的连接
        self.ui.pushButton.clicked.connect(self.clear_textedit_1)            # 实现测报告生成区清除按钮信号与函数槽的连接
        self.ui.pushButton_5.clicked.connect(self.clear_textedit_2)          # 实现系统菜单区清除按钮信号与函数槽的连接
        self.ui.pushButton_3.clicked.connect(self.clear_lineEdit)            # 实现用户输出清除区清除按钮信号与函数槽的连接
        self.ui.pushButton_2.clicked.connect(self.confirm_button_clicked)    # 实现将用户确认按钮信号与函数槽的连接

    def update_output_text_1(self, text):
        self.ui.textEdit.setText(text)

    def update_output_text_2(self, text):
        self.ui.textEdit_2.setText(text)

    def clear_textedit_1(self):
        self.ui.textEdit.clear()
        Menu.output1 = ""

    def clear_textedit_2(self):
        self.ui.textEdit_2.clear()
        Menu.output2 = ""

    def clear_lineEdit(self):
        self.ui.lineEdit.clear()

    def confirm_button_clicked(self):
        text = self.ui.lineEdit.text()
        input_queue.put(text)
        self.ui.lineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
