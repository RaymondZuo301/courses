# -*- coding: utf-8 -*-
def fun(n):
    if n>=90 and n<=100:
        return "A"
    elif n>=70 and n<=89:
        return "B"
    elif n>=60 and n<=69:
        return "C"
    elif n>=0 and n<=599:
        return "D"  
    else:
        return "Invalid score"
while 1:    
    n=input("score:")
    print fun(n)
