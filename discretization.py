# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 15:52:29 2016

@author: Administrator
"""
'''
聚类离散化，最后的result的格式为：
      1           2           3           4
A     0    0.178698    0.257724    0.351843
An  240  356.000000  281.000000   53.000000
即(0, 0.178698]有240个，(0.178698, 0.257724]有356个，依此类推。
'''
#数据聚类离散化

import pandas as pd
from sklearn.cluster import KMeans

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

datafile = 'chapter8/demo/data/data.xls' #待聚类的数据文件
processedfile = 'chapter8/demo/tmp/data_processed.xls' #数据处理后文件

typelabel ={u'肝气郁结证型系数':'A', u'热毒蕴结证型系数':'B', u'冲任失调证型系数':'C', u'气血两虚证型系数':'D', u'脾胃虚弱证型系数':'E', u'肝肾阴虚证型系数':'F'}

k = 4 #需要进行的聚类类别数

#读取数据并进行聚类分析
data=pd.read_excel(datafile,encoding='utf-8')
keys=list(typelabel.keys())
result = pd.DataFrame()

#判断是否主窗口运行，如果是将代码保存为.py后运行，则需要这句，如果直接复制到命令窗口运行，则不需要这句。
if __name__ == '__main__':
    for i in range(len(keys)):
        print(u'正在进行“%s”的聚类...' % keys[i]) #调用k-means算法，进行聚类离散化
        kmodel=KMeans(n_clusters=k,n_jobs=4)
        kmodel.fit(data[[keys[i]]].as_matrix()) #训练模型
        
        r1=pd.DataFrame(kmodel.cluster_centers_,columns=[typelabel[keys[i]]]) #聚类中心
        r2=pd.Series(kmodel.labels_).value_counts() #分类统计
        r2=pd.DataFrame(r2,columns=[typelabel[keys[i]]+'n']) #转为DataFrame，记录各个类别的数目
        r=pd.concat([r1,r2],axis=1).sort(typelabel[keys[i]]) #匹配聚类中心和类别数目
        r.index=[1,2,3,4]
        
        r[typelabel[keys[i]]]=pd.rolling_mean(r[typelabel[keys[i]]],2) #rolling_mean()用来计算相邻2列的均值，以此作为边界点。
        r[typelabel[keys[i]]][1]=0.0
        result=result.append(r.T)
        
    result=result.sort() #以Index排序，即以A,B,C,D,E,F顺序排
    result.to_excel(processedfile)