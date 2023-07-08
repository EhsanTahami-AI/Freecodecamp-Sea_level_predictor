# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:17:49 2023

@author: kanoon
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import sys
import numpy as np

df=pd.read_csv('C:/Users/kanoon/Desktop/freecode camp/5/epa-sea-level.csv')
# df=df.dropna()

slope, intercept, r, p, std_err = stats.linregress(df['Year'][1:135],df['CSIRO Adjusted Sea Level'].dropna())

x1=np.arange(df['Year'].min(),2050,1)
y1=slope*x1+intercept

plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
plt.plot(x1,y1,'r')

df1=df[df['Year']>=2000]

slope, intercept, r, p, std_err = stats.linregress(df1['Year'][1:15],df1['CSIRO Adjusted Sea Level'].dropna())
x2=np.arange(df1['Year'].min(),2050,1)
y2=slope*x2+intercept
plt.plot(x2,y2,'g')
plt.xlabel('Year')
plt.ylabel('Sea level (inches)')
plt.title('Rise in Sea Level')

plt.savefig('C:/Users/kanoon/Desktop/freecode camp/5/Sea level plot', dpi=200)