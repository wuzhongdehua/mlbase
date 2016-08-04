# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 14:25:50 2016

@author: Administrator
"""

#建立、训练多层神经网络，并完成模型的检验

import pandas as pd

inputfile1='chapter10/demo/data/train_neural_network_data.xls' #训练数据
inputfile2='chapter10/demo/data/test_neural_network_data.xls' #测试数据
testoutputfile = 'chapter10/demo/tmp/test_output_data2.xls' #测试数据模型输出文件

data_train = pd.read_excel(inputfile1) #读入训练数据(由日志标记事件是否为洗浴)
data_test = pd.read_excel(inputfile2) #读入测试数据(由日志标记事件是否为洗浴)

y_train = data_train.iloc[:,4].as_matrix() #训练样本标签列
x_train = data_train.iloc[:,5:17].as_matrix() #训练样本特征
y_test = data_test.iloc[:,4].as_matrix() #测试样本标签列
x_test = data_test.iloc[:,5:17].as_matrix() #测试样本特征

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

model = Sequential() #建立模型
model.add(Dense(11, 17)) #添加输入层、隐藏层的连接
model.add(Activation('relu')) #以Relu函数为激活函数
model.add(Dense(17, 10)) #添加隐藏层、隐藏层的连接
model.add(Activation('relu')) #以Relu函数为激活函数
model.add(Dense(10, 1)) #添加隐藏层、输出层的连接
model.add(Activation('sigmoid')) #以sigmoid函数为激活函数
#编译模型，损失函数为binary_crossentropy，用adam法求解
model.compile(loss='binary_crossentropy', optimizer='adam', class_mode="binary") 

model.fit(x_train, y_train, nb_epoch = 100, batch_size = 1) #训练模型
model.save_weights('chapter10/demo/tmp/net2.model') #保存模型参数
#model.load_weights('chapter10/demo/tmp/net.model')

r = pd.DataFrame(model.predict_classes(x_test), columns = [u'预测结果'])
pd.concat([data_test.iloc[:,:5], r], axis = 1).to_excel(testoutputfile)
model.predict(x_test)