# -*- coding: utf-8 -*-

from numpy import array2string
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from featurepossess import generate_crlf
import joblib
import control


def logistic_crlf_train(signal1, signal2):
    crlf_matrix = generate_crlf("./data/logistic/crlf/crlf_train.csv", "./data/logistic/crlf/crlf_matrix.csv", 1)
    crlf_normal_matrix = generate_crlf("./data/logistic/crlf/normal_train.csv", "./data/logistic/crlf/crlf_normal_matrix.csv", 0)

    df = pd.read_csv(crlf_matrix)
    df.to_csv("./data/logistic/crlf/all_matrix.csv", encoding="utf_8_sig", index=False)
    df = pd.read_csv(crlf_normal_matrix)
    df.to_csv("./data/logistic/crlf/all_matrix.csv", encoding="utf_8_sig", index=False, header=False, mode='a+')

    feature_max = pd.read_csv('./data/logistic/crlf/all_matrix.csv')
    arr = feature_max.values
    data = np.delete(arr, -1, axis=1)   # 删除最后一列
    target = arr[:, 3]
    # 随机划分训练集和测试集
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.3, random_state=6)
    # 模型
    logistic = LogisticRegression(max_iter=10000)   # 创建分类器对象，
    logistic.fit(train_data, train_target)  # 训练模型
    joblib.dump(logistic, './model/logistic_crlf.model')
    y_pred = logistic.predict(test_data)    # 预测
    # Verify
    control.Menu.output1 += "*" * control.N + "\n"
    control.Menu.output1 += "逻辑回归模型CRLF注入攻击训练结果报告\n"
    control.Menu.output1 += "本次训练共有%d条数据用于测试" % len(y_pred) + '\n'
    control.Menu.output1 += '准确度为:{:.1%}' .format(metrics.precision_score(y_true=test_target, y_pred=y_pred)) + '\n'
    control.Menu.output1 += '召回率为:{:.1%}' .format(metrics.recall_score(y_true=test_target, y_pred=y_pred)) + '\n'
    control.Menu.output1 += 'F1的值为:{:.1%}' .format(metrics.f1_score(y_true=test_target, y_pred=y_pred)) + '\n'
    control.Menu.output1 += "混淆矩阵如下所示:\n"
    confusion_matrix_str = array2string(metrics.confusion_matrix(y_true=test_target, y_pred=y_pred))
    control.Menu.output1 += confusion_matrix_str + '\n'
    control.Menu.output1 += "*" * control.N + "\n"
    control.Menu.output1 += '\n'
    signal1.emit(control.Menu.output1)
