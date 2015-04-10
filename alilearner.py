# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:39:39 2015

@author: xujingping
"""
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier

from sklearn.cross_validation import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

import pandas as pd

def load_data(x1,y1,x2,y2):
    train_feature=pd.reac_csv(x1)
    train_label=pd.reac_csv(y1)
    test_feature=pd.reac_csv(x1)
    test_label=pd.reac_csv(y1)
    #filter
    result=[train_feature,train_label,test_feature,test_label]
    return result
    
if __name__=="__main__":
    df=pd.read_csv('featues_train.csv')
    y=df['label'].values
    del df['user_id']
    del df['item_id']
    del df['label']
    X=df.values
    clf = DecisionTreeClassifier(max_depth=None, min_samples_split=1,  random_state=0)
    
    clf.fit( X, y)
    joblib.dump(clf, 'filename.txt') 
    clf = joblib.load('filename.pkl') 
    

 