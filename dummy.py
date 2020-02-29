#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:21:27 2019

@author: hassan
"""
# dummy variables from pandas 


print(pd.get_dummies(Y))
print(pd.get_dummies(dataset['Country']))
dataset.head(10)
Country_dummies = pd.get_dummies(dataset.Country).iloc[:,:3]
Purchased_dummies = pd.get_dummies(dataset.Purchased).iloc[:,:2]







