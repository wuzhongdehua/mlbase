# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:05:58 2016

@author: Administrator
"""

from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np

ADF(np.random.rand(100))