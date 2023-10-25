from user_test import user_test
from test import test
from Normal_KNN import knn_normal_train
from Normal_Logistic import logistic_normal_train
from Sql_KNN import knn_sql_train
from Sql_Logistic import logistic_sql_train
from Xss_KNN import knn_xss_train
from Xss_Logistic import logistic_xss_train
from Traversal_KNN import knn_traversal_train
from Traversal_Logistic import logistic_traversal_train
from CRLF_KNN import knn_crlf_train
from CRLF_Logistic import logistic_crlf_train
from train import train
from PyQt6.QtCore import QThread, pyqtSignal
import queue

function_knn_dic = {1: knn_normal_train, 2: knn_sql_train, 3: knn_xss_train,
                    4: knn_traversal_train, 5: knn_crlf_train}

function_logistic_dic = {1: logistic_normal_train, 2: logistic_sql_train, 3: logistic_xss_train,
                         4: logistic_traversal_train, 5: logistic_crlf_train}


input_queue = queue.Queue()
N = 52


class Menu(QThread):
    # 定义信号
    textbox1 = pyqtSignal(str)
    textbox2 = pyqtSignal(str)
    output1 = ""
    output2 = ""

    def run(self):
        while (1):
            Menu.output2 += "*" * N + "\n"
            Menu.output2 += "欢迎使用基于机器学习的恶意流量检测系统\n"
            Menu.output2 += "请选择要使用的功能\n"
            Menu.output2 += "1. 训练数据集并测试      2. 使用本地测试集进行测试\n"
            Menu.output2 += "3. 使用用户提供URL进行测试      4. 退出\n"
            Menu.output2 += "*" * N + "\n"
            Menu.output2 += '\n'

            # 发送信号，将输出实时更新到文本框中
            self.textbox2.emit(Menu.output2)
            # 等待主线程传来的数据
            choose = input_queue.get()
            self.textbox2.emit(Menu.output2)
            if int(choose) == 4:
                break
            elif int(choose) == 1:
                train(self.textbox1, self.textbox2)
            elif int(choose) == 2:
                test(self.textbox1, self.textbox2)
            elif int(choose) == 3:
                user_test(self.textbox1, self.textbox2)
            else:
                break

