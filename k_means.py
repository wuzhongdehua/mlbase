# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 10:54:37 2016

@author: Administrator
"""

import pandas as pd

#参数初始化
inputfile = 'ch5/data/consumption_data.xls' #销量及其他属性数据
outputfile = 'ch5/tmp/data_type.xls' #保存结果的文件名
k=3
iteration=500
data=pd.read_excel(inputfile,index_col='Id')
data_sz=1.0*(data-data.mean())/data.std() #数据标准化

from sklearn.cluster import KMeans
model=KMeans(n_clusters=k,n_jobs=4,max_iter=iteration) #分为K类，并发数4
model.fit(data_sz)

#简单打印
r1=pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2=pd.DataFrame(model.cluster_centers_) #找出聚类的中心
r=pd.concat([r1,r2],axis=1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns=list(data.columns)+u'类别数目' #重命名表开头

r=pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1) #详细输出每个样本对应的类别信息
r.columns=list(data.cloumns)+u'聚类类别' #重命名表头
r.to_excel(outputfile)

def density_plot(data,title):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    plt.figure()
    for i in range(len(data.iloc[0])):
        (data.iloc[:,i]).plot(kind='kde',label=data.columns[i],linewidth=2)
    plt.ylabel(u'密度')
    plt.xlabel(u'人数')
    plt.title(u'聚类类别%s各个属性')
    plt.legend()
    return plt
    
def density_plot(data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    p=data.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend()
    return plt
    
pic_output='ch5/tmp/pd_' #概率密度图文件名前缀
for i in range(k):
    density_plot(data[r[u'聚类类别']==i]).savefig(u'%s%s.png' %(pic_output, i))