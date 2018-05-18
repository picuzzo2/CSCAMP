# -*- coding: utf-8 -*-
# @Author: CSB307
# @Date:   2018-05-17 09:24:41
# @Last Modified by:   CSB307
# @Last Modified time: 2018-05-18 15:55:49

import numpy as np
import pandas as pd
#from multi_column_label_encoder import MultiColumnLabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn import linear_model
#import code

def predicted():
    dataset = pd.read_csv('winequality.csv')
    test_dataset = pd.read_csv('collectedData.csv')
    #dataset = dataset.drop(['name','mfr'],1)

    y = np.array(dataset['quality'])
    dataset = dataset.drop(['quality','density','pH'],1)
    #dataset = MultiColumnLabelEncoder([i for i in dataset if dataset[i].dtypes ==object]).fit_transform(dataset)

    x = np.array(dataset)
    x_train = x
    x_test = np.array(test_dataset)
    #x_test = [int(i) for i in x_test]
    #x_text = np.array(x_test).reshape(-1,1)
    y_train = y
    #y_test = y[1590:]
    #x_train, x_test,y_train, y_test = train_test_split(x, y, test_size=0.2)

    regr = linear_model.LinearRegression()
    regr.fit(x_train,y_train)

    #print(dataset)

    #print('Normalized')
    #print(x)

    #print('\nPrediction')
    prediction = regr.predict(x_test)
#print(prediction)


    return prediction

#print(predicted())
#print('\nR2 Score')
#score = r2_score(y_test,prediction)
#print(score)   

#print(predicted())

#print(x_test)
#print(x_train, x_test,y_train, y_test)