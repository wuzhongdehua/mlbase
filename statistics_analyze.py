# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:01:13 2016

@author: Administrator
"""

import pandas as pd

catering_sale = 'demo/data/catering_sale.xls' #餐饮数据
data=pd.read_excel(catering_sale, index_col=u'日期')
data=data[(data[u'销量'] > 400)&(data[u'销量'] < 5000)]
statistics=data.describe()

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位数间距

print statistics

#==============================================================================
# count   195.000000
# mean   2744.595385
# std     424.739407
# min     865.000000
# 25%    2460.600000
# 50%    2655.900000
# 75%    3023.200000
# max    4065.200000
# range  3200.200000
# var       0.154755
# dis     562.600000
#==============================================================================
