#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:33:19 2023

@author: arnavboppudi
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Orientation/2023-06-13-survey.csv")
plt.hist(data.iloc[:, 3], bins = 30, color = 'red', alpha = 0.7)


plt.xlabel("GB")
plt.ylabel('# of Students')
plt.title('Histogram of RAM in GB')













