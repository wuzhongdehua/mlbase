# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:26:53 2016
利用小波分析进行特征分析
@author: Administrator
"""

inputfile= 'ch4/data/leleccum.mat' #提取自Matlab的信号文件

from scipy.io import loadmat #mat是MATLAB专用格式，需要用loadmat读取它
mat=loadmat(inputfile)
signal=mat['leleccum'][0]

import pywt #导入PyWavelets
coeffs=pywt.wavedec(signal,'bior3.7',level=5)
#返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组
print coeffs