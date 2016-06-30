# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:19:21 2016

@author: Administrator
"""

from sklearn.linear_model import LinearRegression
from sklearn import datasets

#model = LinearRegression()
#print(model)

iris=datasets.load_iris
print(iris.data.shape)

from sklearn import svm
clf=svm.LinearSVC()
clf.fit(iris.data,iris.target)
clf.predict([[5.0,3.6,1.3,0.25]])
clf.coef_