# -*- coding: utf-8 -*-
def fib1(n):
    if(n-1==0 or n-1==1):
        return n-1
    else:
        a,b=0,1
        i=2
        while(i<n):
            a,b=b,a+b
            i+=1
        return b
def fib2(n):
    if(n-1==0 or n-1==1):
        return n-1
    else:
        return fib2(n-1)+fib2(n-2)
def fib(n):
    i=1
    while i<=n:
        print fib1(i),fib2(i)
        i+=1

while 1:
    x=input('输出斐波那契数列的前多少个数？')
    fib(x)

