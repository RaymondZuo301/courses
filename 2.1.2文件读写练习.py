# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:24:03 2016

@author: ZFR-64SSD
"""
f1=open('src.txt','w+',0)
f1.write('How many seas must a white dove sail\nBefore she sleeps in the sand\n')
f1.seek(0, 0)
s=f1.readlines()
f1.close()
f2=open('dest.txt','w+',0)
f2.writelines(s)
f2.seek(0, 0)
s=f2.readlines()
f2.close()
f2=open('dest.txt','w+',0)
ss='How many roads must a man walk down\nBefore they call him a man\n'
f2.write(ss)
f2.writelines(s)
f2.close()
