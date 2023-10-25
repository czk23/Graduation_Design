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
import control

function_knn_dic = {1: knn_normal_train, 2: knn_sql_train, 3: knn_xss_train,
                    4: knn_traversal_train, 5: knn_crlf_train}

function_logistic_dic = {1: logistic_normal_train, 2: logistic_sql_train, 3: logistic_xss_train,
                         4: logistic_traversal_train, 5: logistic_crlf_train}


def train(signal1, signal2):
    while(1):

        control.Menu.output2 += "*" * control.N + "\n"
        control.Menu.output2 += "请选择要进行训练的模型\n"
        control.Menu.output2 += "1. KNN模型     2. 逻辑回归模型      3. 退出\n"
        control.Menu.output2 += "*" * control.N + "\n"
        control.Menu.output2 += '\n'

        signal2.emit(control.Menu.output2)

        model = control.input_queue.get()
        if int(model) == 3:
            break
        elif int(model) == 1:

            control.Menu.output2 += "*" * control.N + "\n"
            control.Menu.output2 += "请选择进行训练的数据类型\n"
            control.Menu.output2 += "1. 正常流量      2. SQL注入攻击      3. XSS攻击\n"
            control.Menu.output2 += "4. 目录遍历攻击   5. CRLF注入攻击     6. 退出\n"
            control.Menu.output2 += "*" * control.N + "\n"
            control.Menu.output2 += '\n'
            signal2.emit(control.Menu.output2)
            kind = control.input_queue.get()
            if int(kind) == 6:
                break
            elif 1 <= int(kind) <= 5:
                function_knn_dic[int(kind)](signal1, signal2)
            else:
                break
        elif int(model) == 2:

            control.Menu.output2 += "*" * control.N + "\n"
            control.Menu.output2 += "请选择进行训练的数据类型\n"
            control.Menu.output2 += "1. 正常流量      2. SQL注入攻击      3. XSS攻击\n"
            control.Menu.output2 += "4. 目录遍历攻击   5. CRLF注入攻击     6. 退出\n"
            control.Menu.output2 += "*" * control.N + "\n"
            control.Menu.output2 += '\n'
            signal2.emit(control.Menu.output2)
            kind = control.input_queue.get()
            if int(kind) == 6:
                break
            elif 1 <= int(kind) <= 5:
                function_logistic_dic[int(kind)](signal1, signal2)
            else:
                break
        else:
            break
