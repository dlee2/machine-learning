# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:31:48 2015
website:
http://connor-johnson.com/2014/02/18/linear-regression-with-python/
@author: Dan
"""

import numpy as np
import pandas as pd
import statsmodels
from sklearn.linear_model import LinearRegression
import scipy,scipy.stats

data_str = '''Region Alcohol Tobacco
North 6.47 4.03
Yorkshire 6.13 3.76
Northeast 6.19 3.77
East Midlands 4.89 3.34
West Midlands 5.63 3.47
East Anglia 4.52 2.92
Southeast 5.89 3.20
Southwest 4.79 2.71
Wales 5.27 3.53
Scotland 6.08 4.51
Northern Ireland 4.02 4.56'''

d = data_str.split('\n')
d = [i.split(' ') for i in d]


df = pd.DataFrame(d[1:], columns = d[0])