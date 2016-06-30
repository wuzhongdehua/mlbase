# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:19:33 2016

@author: Administrator
"""

import pandas as pd

#参数初始化
inputfile= 'ch4/data/electricity_data.xls' #供入供出电量数据
outputfile = 'ch4/tmp/electricity_data.xls' #属性构造后数据文件

data=pd.read_excel(inputfile)
data[u'线损率']=(data[u'供入电量']-data[u'供出电量']) / data[u'供入电量']

data.to_excel(outputfile,index=False)