# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from featurepossess import generate_abnormal
import joblib


def logistic_normal_train():
    normal_matrix = generate_abnormal("./data/logistic/normal/normal_train.csv", "./data/logistic/normal/normal_matrix.csv", 1)
    abnormal_matrix = generate_abnormal("./data/logistic/normal/abnormal_train.csv", "./data/logistic/normal"
                                                                                     "/abnormal_matrix.csv", 0)

    df = pd.read_csv(normal_matrix)
    df.to_csv("./data/logistic/normal/all_matrix.csv", encoding="utf_8_sig", index=False)
    df = pd.read_csv(abnormal_matrix)
    df.to_csv("./data/logistic/normal/all_matrix.csv", encoding="utf_8_sig", index=False, header=False, mode='a+')

    feature_max = pd.read_csv('./data/logistic/normal/all_matrix.csv')
    arr = feature_max.values
    data = np.delete(arr, -1, axis=1)               # 删除最后一列
    target = arr[:, 13]
    # 随机划分训练集和测试集
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.3, random_state=6)
    # 模型
    logistic = LogisticRegression(max_iter=10000)   # 创建分类器对象，
    logistic.fit(train_data, train_target)          # 训练模型
    joblib.dump(logistic, './model/logistic_normal.model')
    # print("logistic_normal model has been saved to 'model/logistic_normal.model'")
    y_pred = logistic.predict(test_data)            # 预测
    # print("y_pred:%s" % y_pred)
    # print("test_target:%s" % test_target)
    # Verify
    print("*" * 42)
    print("逻辑回归模型正常流量训练结果报告")
    print("本次训练共有%d条数据用于测试" % len(y_pred))
    print('准确度为:{:.1%}' .format(metrics.precision_score(y_true=test_target, y_pred=y_pred)))  # 准确率
    print('召回率为:{:.1%}' .format(metrics.recall_score(y_true=test_target, y_pred=y_pred)))     # 召回率
    print('F1的值为:{:.1%}' .format(metrics.f1_score(y_true=test_target, y_pred=y_pred)))         # F1的值
    print("混淆矩阵如下所示:")
    print(metrics.confusion_matrix(y_true=test_target, y_pred=y_pred))  # 混淆矩阵
    print("*" * 42)
