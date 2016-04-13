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
start = (today.year-2, today.month,today.day)
quotesMS = quotes_historical_yahoo('MSFT',start,today)
lable = ['data','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS,columns=lable)
list = []
for i in range(0,len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x,'%y/%m/%d')
    list.append(y)
quotesdfMS.index = list
#print quotesdfMS
quotesdfMS = quotesdfMS.drop()