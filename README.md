# 摘要
&ensp; &ensp; &ensp;网络信息技术的快速发展和相关服务的广泛应用，在推动着社会经济的快速发展的同时，也暴露许多网络安全方面暗藏的漏洞，恶意流量检测成为了网络安全中的一个重要问题。因此，一种基于机器学习的恶意流量检测系统被提出，该系统利用机器学习算法对网络流量进行分类，可以有效地识别恶意流量。  
&ensp; &ensp; &ensp;系统包括三大功能：不同算法不同种类流量的训练功能、本地测试集测试功能、用户输入数据测试功能。系统选择了KNN算法和逻辑回归算法作为系统的机器学习核心算法，因为不同种类流量的特征向量维度很难保持一致，所以根据五种不同的数据类型和两种不同的算法得到了共十种二分类训练模型。系统首先在github上收集到了相关的恶意流量payloads，其中恶意流量包括SQL注入攻击、XSS攻击、目录遍历攻击和CRLF注入攻击；在HTTP DATASET CSIC 2010数据集中选取部分作为系统正常流量数据集，并从中的http请求中提取出其URL作为数据对象。然后根据不同种类流量的特点分别进行特征提取工作，根据得到的特征向量分别利用KNN算法和逻辑回归算法进行不同模块的训练得到相应的模块并保存。系统可以根据用户不同的选择接受不同的测试集来进行测试，最终根据测试结构生成一份测试报告，其中包括了本次测试的准确率、回归率等信息。除此之外，系统还设计了与用户的交互功能，当用户输入单个URL让系统进行判断时，系统会将测试结果输出给用户并让用户进行是否准确的反馈，若用户判断本次测试准确系统会将此次测试的URL加入的训练集中并重新训练。  
&ensp; &ensp; &ensp;系统最终测试结果显示，无论是训练数据，本地测试数据集还是用户测试数据集，KNN算法的精确率、召回率和F1值总体上都比逻辑回归算法高，并且两个算法的精确率、召回率和F1值整体都在90%以上，表明了系统良好的实现效果。
