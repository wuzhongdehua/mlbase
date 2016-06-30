# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:30:12 2016
主成分分析 降维
@author: Administrator
"""

import pandas as pd

#参数初始化
inputfile = 'ch4/data/principal_component.xls'
outputfile = 'ch4/tmp/dimention_reducted.xls' #降维后的数据

data=pd.read_excel(inputfile,header=None)

from sklearn.decomposition import PCA

pca=PCA()
pca.fit(data)
print '各个特征向量\n'
print pca.components_ #返回模型的各个特征向量
print '各自的方差百分比\n'
print pca.explained_variance_ratio_ #返回各个成分各自的方差百分比
#==============================================================================
# [  7.74011263e-01   1.56949443e-01   4.27594216e-02   2.40659228e-02
#    1.50278048e-03   4.10990447e-04   2.07718405e-04   9.24594471e-05]
#==============================================================================
#有上面结果可以判断保留的维度是3
pca=PCA(3)
pca.fit(data)
low_d=pca.transform(data) #降维
pd.DataFrame(low_d).to_excel(outputfile) #保存结果
pca.inverse_transform(low_d) #必要时可以用inverse_transform()函数来复制数据
print '降维结果:'
print low_d