# -*- coding: utf-8 -*-
from math import sqrt
def sushu1(x):
    if x==1:
        return False
    k=int(sqrt(x))
    for j in range(2,k+1):
       if x%j==0:
           return False
    return True
def sushu2(x):
    if x==1:
        return False
    k= (sqrt(x))
    j=2
    while(j<=k):
        if x%j==0:
            return False
        j+=1
    return True
for i in range(1,101):
    if sushu1(i):
        print i
    if sushu2(i):
        print " %d "%i
        
