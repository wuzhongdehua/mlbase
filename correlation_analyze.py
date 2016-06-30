# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:21:03 2016

@author: cxy
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

catering_sale = 'demo/data/catering_sale_all.xls' #餐饮数据，含有其他属性
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列

#print data.mean()
#print data.cov()

#data.corr() #相关系数矩阵，即给出了任意两款菜式之间的相关系数
#2print data.corr()[u'百合酱蒸凤爪'] #只显示“百合酱蒸凤爪”与其他菜式的相关系数

#print data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']) #计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数

#D=pd.DataFrame([range(1,8),range(2,9)])
#print D.corr(method='spearman')
#S1=D.loc[0]
#S2=D.loc[1]
#print S1.corr(S2,method='pearson')

#import numpy as np
#
#D=pd.DataFrame(np.random.rand(6,5))#产生6x5的随机矩阵
#print D.cov()

#D=pd.DataFrame(np.random.rand(6,5))#产生6x5的随机矩阵
#print D.skew()

#D=pd.Series(range(0,20))
#print D.cumsum()
#print pd.rolling_sum(D,2)


#plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
#plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#plt.figure(figsize=(7,5))



#x=np.linspace(0.2*np.pi,50)
#y=np.sin(x)
#plt.plot(x,y,'bp--')
#plt.show()

#labels='Frogs','Hogs','Dogs','Logs'
#sizes=[15,30,45,10]
#colors=['yellowgreen','gold','lightskyblue','lightcoral']
#explode=(0,0.1,0,0)
#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
#plt.axis('equal')
#plt.show()

#x=np.random.rand(1000)
#plt.hist(x,10)
#plt.show()

#x=np.random.rand(1000)
#D=pd.DataFrame([x,x+1]).T #构造两列的DataFramme
#D.plot(kind='box')
#plt.show()


#plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
#plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#x=pd.Series(np.exp(np.arange(20)))
#x.plot(label=u'原始数据图',legend=True)
#plt.show()
#x.plot(logy=True,label=u'对数数据图',legend=True)
#plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
error=np.random.rand(10)
y=pd.Series(np.sin(np.arange(10)))
y.plot(yerr=error)
plt.show()