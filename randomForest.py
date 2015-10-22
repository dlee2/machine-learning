# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:10:26 2015

@author: Dan
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
df['train'] = np.random.uniform(0,1,len(df)) <= .75
df['species'] = pd.Factor(iris.target, iris.target_names)