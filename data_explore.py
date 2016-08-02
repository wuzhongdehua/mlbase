# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:48:57 2016

@author: Administrator
"""

#对数据进行基本的探索
#返回缺失值个数以及最大最小值

import pandas as pd

datafile= 'chapter7/demo/data/air_data.csv' #航空原始数据,第一行为属性标签
resultfile = 'chapter7/demo/tmp/explore.xls' #数据探索结果表

 #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data = pd.read_csv(datafile, encoding = 'utf-8')
#包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
explore=data.describe(percentiles = [], include='all').T
#describe()函数自动计算非空值数，需要手动计算空值数
explore['null']=len(data)-explore['count']

explore=explore[['null','max','min']]
#表头重命名
explore.columns=[u'空值数',u'最大值',u'最小值']

explore.to_excel(resultfile) #导出结果