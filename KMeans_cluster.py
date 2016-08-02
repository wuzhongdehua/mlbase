# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 15:38:26 2016

@author: Administrator
"""

#K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans

inputfile = 'chapter7/demo/tmp/zscoreddata.xls' #待聚类的数据文件
k = 5                       #需要进行的聚类类别数

#读取数据并进行聚类分析
data = pd.read_excel(inputfile) #读取数据

#调用k-means算法，进行聚类分析
#n_jobs是并行数，一般等于CPU数较好
kmodel=KMeans(n_clusters=k,n_jobs = 2)

kmodel.fit(data) #训练模型

print kmodel.cluster_centers_ #查看聚类中心
print kmodel.labels_ #查看各样本对应的类别