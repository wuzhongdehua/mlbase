# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:06:42 2016
拉格朗日插值法

@author: Administrator
"""

import pandas as pd
from scipy.interpolate import lagrange#导入拉格朗日差值函数

inputfile = 'ch4/data/catering_sale.xls' #销量数据路径
outputfile = 'ch4/tmp/sales.xls' #输出数据路径

data=pd.read_excel(inputfile)#读入数据
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)]=None##过滤异常值，将其变为空值

#自定义差值函数
#s为列向量，n为被差值的位置，k为取值前后的数据个数，默认为s
def ployinterp_column(s,n,k=5):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]#取数
    y=y[y.notnull()]#踢出空值
    return lagrange(y.index,list(y))(n)
    
#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:#如果为空即插值
            data[i][j]=ployinterp_column(data[i],j)
            
data.to_excel(outputfile)