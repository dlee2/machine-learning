# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:10:26 2015
tutorial on website:
http://blog.yhathq.com/posts/random-forests-in-python.html
@author: Dan
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
df['train'] = np.random.uniform(0,1,len(df)) <= .75
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

df.head()

train, test = df[df['train']== True], df[df['train']==False]

features = df.columns[:4]
clf = RandomForestClassifier(n_jobs = 2)

y,_ = pd.factorize(train['species'])
clf.fit(train[features], y)

preds = iris.target_names[clf.predict(test[features])]
pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])
