# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:22:59 2016
"""
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
from datetime import datetime
import pandas as pd
import time
today = date.today()
start = (today.year-3, today.month,today.day)
quotesMS = quotes_historical_yahoo('MSFT',start,today)
lable = ['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS,columns=lable)
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
print quotesdfMS14.groupby('month').mean().close

