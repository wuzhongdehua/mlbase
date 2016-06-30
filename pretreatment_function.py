# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:11:57 2016
预处理函数
@author: Administrator
"""

import numpy as np
import pandas as pd
from scipy.interpolate import lagrange

D=pd.Series([1,1,2,3,5])
#print D.unique()
#print np.unique(D)

#print np.random.rand(4,4,5,6) #随机矩阵
print np.random.randn(4,4,5,6) #随机矩阵(服从正态分布)