# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 15:23:05 2016

@author: AtoZ
"""
import re

f = open('regex_sum_238753.txt', 'r', 0)
f.readline()
num = []
sum = 0
for i in f:
    temp = re.findall('[0-9]+',i)
    num.extend(temp)
for i in num:
    sum += int(i)
print sum