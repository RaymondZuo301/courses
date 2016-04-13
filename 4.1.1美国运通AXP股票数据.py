# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 11:01:51 2016
"""
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
from datetime import datetime
import pandas as pd
import time
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo('axp', start, today)
fields = ['date','open','close','high','low','volume']
list1 = []
for i in range(0,len(quotes)):
    x=date.fromordinal(int(quotes[i][0]))
    y=datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf = pd.DataFrame(quotes,index=list1,columns = fields)
quotesdf = quotesdf.drop(['date'],axis=1)
#ptint quotesdf #输出数据
listtemp = []
for i in range(0,len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],'%Y-%m-%d')
    listtemp.append(temp.tm_mon)
tempdf=quotesdf.copy()
tempdf['month']=listtemp
#print tempdf['month'].value_counts() #输出每月开盘天数
#print tempdf.groupby('month').count() #用groupby实现统计每月开盘天数
