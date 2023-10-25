# -*- coding: utf-8 -*-

from numpy import array2string
import numpy as np
import pandas as pd
from sklearn import metrics
from featurepossess import generate_abnormal
from featurepossess import generate_sql
from featurepossess import generate_xss
from featurepossess import generate_traversal
from featurepossess import generate_crlf
import joblib
import control

normal_dir = "./data/test/normal/normal_test.csv"
sql_dir = "./data/test/sql/sql_test.csv"
xss_dir = "./data/test/xss/xss_test.csv"
traversal_dir = "./data/test/traversal/traversal_test.csv"
crlf_dir = "./data/test/crlf/crlf_test.csv"


my_dic = {1: {1: "KNN模型正常流量", 2: "KNN模型SQL注入攻击流量", 3: "KNN模型XSS攻击模型流量", 4: "KNN模型目录遍历攻击流量", 5: "KNN模型CRLF注入攻击流量"},
          2: {1: "逻辑回归模型正常流量", 2: "逻辑回归模型SQL注入攻击流量", 3: "逻辑回归模型XSS攻击模型流量", 4: "逻辑回归模型目录遍历攻击流量", 5: "逻辑回归模型CRLF注入攻击流量"}}


# 函数从该文件中读取测试数据，并将其分成特征矩阵和目标向量两部分
def gen_data(allm_dir):
    feature_max = pd.read_csv(allm_dir)
    arr = feature_max.values
    data = np.delete(arr, -1, axis=1)  # 删除最后一列
    test_target = arr[:, 7]
    return data, test_target


def gen_data_crlf(allm_dir):
    feature_max = pd.read_csv(allm_dir)
    arr = feature_max.values
    data = np.delete(arr, -1, axis=1)  # 删除最后一列
    test_target = arr[:, 3]
    return data, test_target


def gen_data_xss(allm_dir):
    feature_max = pd.read_csv(allm_dir)
    arr = feature_max.values
    data = np.delete(arr, -1, axis=1)  # 删除最后一列
    test_target = arr[:, 3]
    return data, test_target


def gen_data_normal(allm_dir):
    feature_max = pd.read_csv(allm_dir)
    arr = feature_max.values
    data = np.delete(arr, -1, axis=1)  # 删除最后一列
    test_target = arr[:, 13]
    return data, test_target


def Normal(model):
    normal_test_matrix = generate_abnormal(normal_dir, "./data/test/normal/normal_test_matrix.csv", 1)
    if model == 1:
        clf = joblib.load("./model/knn_normal.model")
    else:
        clf = joblib.load("./model/logistic_normal.model")
    return normal_test_matrix, clf


def Sql(model):
    sql_test_matrix = generate_sql(sql_dir, "./data/test/sql/sql_test_matrix.csv", 1)
    if model == 1:
        clf = joblib.load("./model/knn_sql.model")
    else:
        clf = joblib.load("./model/logistic_sql.model")
    return sql_test_matrix, clf


def Xss(model):
    xss_test_matrix = generate_xss(xss_dir, "./data/test/xss/xss_test_matrix.csv", 1)
    if model == 1:
        clf = joblib.load("./model/knn_xss.model")
    else:
        clf = joblib.load("./model/logistic_xss.model")
    return xss_test_matrix, clf


def Traversal(model):
    traversal_test_matrix = generate_traversal(traversal_dir, "./data/test/traversal/traversal_test_matrix.csv", 1)
    if model == 1:
        clf = joblib.load("./model/knn_traversal.model")
    else:
        clf = joblib.load("./model/logistic_traversal.model")
    return traversal_test_matrix, clf


def Crlf(model):
    crlf_test_matrix = generate_crlf(crlf_dir, "./data/test/crlf/crlf_test_matrix.csv", 1)
    if model == 1:
        clf = joblib.load("./model/knn_crlf.model")
    else:
        clf = joblib.load("./model/logistic_crlf.model")
    return crlf_test_matrix, clf


def choose_model(signal1, signal2):
    control.Menu.output2 += "*" * control.N + "\n"
    control.Menu.output2 += "请输入要进行哪种模块的测试" + '\n'
    control.Menu.output2 += "1.KNN模型    2.逻辑回归模型    3.退出" + '\n'
    control.Menu.output2 += "*" * control.N + "\n"
    control.Menu.output2 += '\n'
    signal2.emit(control.Menu.output2)
    Model = control.input_queue.get()
    if int(Model) == 1:
        res = 1
    elif int(Model) == 2:
        res = 2
    elif int(Model) == 3:
        res = 3
    else:
        res = 0
    return res


# 字典
switch = {
    1: Normal,
    2: Sql,
    3: Xss,
    4: Traversal,
    5: Crlf
}


def test(signal1, signal2):
    while (1):
        f = choose_model(signal1, signal2)
        if f == 3:
            break
        while f == 0:
            f = choose_model(signal1, signal2)
        control.Menu.output2 += "*" * control.N + "\n"
        control.Menu.output2 += "请输入要进行哪种攻击的检测" + '\n'
        control.Menu.output2 += "1.正常流量       2.sql注入攻击       3.xss攻击" + '\n'
        control.Menu.output2 += "4.目录遍历攻击    5.crlf注入攻击      6.退出" + '\n'
        control.Menu.output2 += "*" * control.N + "\n"
        control.Menu.output2 += '\n'
        signal2.emit(control.Menu.output2)
        flag = control.input_queue.get()
        if int(flag) == 6:
            break
        if int(flag) < 1 or int(flag) > 6:
            continue
        mode, clf = switch.get(int(flag))(f)
        if int(flag) == 5:
            test_data, test_target = gen_data_crlf(mode)
        elif int(flag) == 1:
            test_data, test_target = gen_data_normal(mode)
        elif int(flag) == 3:
            test_data, test_target = gen_data_xss(mode)
        else:
            test_data, test_target = gen_data(mode)
        y_pred = clf.predict(test_data)

        control.Menu.output1 += "*" * control.N + "\n"
        control.Menu.output1 += "%s测试结果报告" % my_dic[int(f)][int(flag)] + '\n'
        control.Menu.output1 += "本次测试共有%d条数据用于测试" % len(y_pred) + '\n'
        control.Menu.output1 += '准确度为:{:.1%}'.format(metrics.precision_score(y_true=test_target, y_pred=y_pred)) + '\n'
        control.Menu.output1 += '召回率为:{:.1%}'.format(metrics.recall_score(y_true=test_target, y_pred=y_pred)) + '\n'
        control.Menu.output1 += 'F1的值为:{:.1%}'.format(metrics.f1_score(y_true=test_target, y_pred=y_pred)) + '\n'
        control.Menu.output1 += "混淆矩阵如下所示:" + '\n'
        confusion_matrix_str = array2string(metrics.confusion_matrix(y_true=test_target, y_pred=y_pred))
        control.Menu.output1 += confusion_matrix_str + '\n'
        control.Menu.output1 += "*" * control.N + "\n"
        control.Menu.output1 += '\n'
        signal1.emit(control.Menu.output1)

