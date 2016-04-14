# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:10:51 2016
"""
import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

today = date.today()
start = (today.year-3, today.month,today.day)
quotesMS = quotes_historical_yahoo_ochl('MSFT',start,today)
quotesIN = quotes_historical_yahoo_ochl('INTC',start,today)
lable = ['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS,columns=lable)
quotesdfIN = pd.DataFrame(quotesIN,columns=lable)
###
list1 = []
for i in range(0,len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x,'%y/%m/%d')
    list1.append(y)
quotesdfMS.index = list1
quotesdfMS = quotesdfMS.drop(['date'],axis = 1)
list1 = []
quotesdfMS14 = quotesdfMS['14/01/01':'14/12/31']
for i in range(0, len(quotesdfMS14)):
    list1.append(int(quotesdfMS14.index[i][3:5]))
quotesdfMS14['month'] = list1
###
list2 = []
for i in range(0,len(quotesIN)):
    x = date.fromordinal(int(quotesIN[i][0]))
    y = date.strftime(x,'%y/%m/%d')
    list2.append(y)
quotesdfIN.index = list2
quotesdfIN = quotesdfIN.drop(['date'],axis = 1)
list2 = []
quotesdfIN14 = quotesdfIN['14/01/01':'14/12/31']
for i in range(0, len(quotesdfIN14)):
    list2.append(int(quotesdfIN14.index[i][3:5]))
quotesdfIN14['month'] = list2
list3=[1,2,3,4,5,6,7,8,9,10,11,12]
pl.subplot(211)
plt.plot(list3,quotesdfMS14.groupby('month').max().close,color='r',marker='o')
pl.subplot(212)
plt.plot(list3,quotesdfIN14.groupby('month').max().close,color='green',marker='o')
