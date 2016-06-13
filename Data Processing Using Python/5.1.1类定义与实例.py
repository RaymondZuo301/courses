# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:55:13 2016
"""

class Dog(object):
	counter = 0
	def __init__(self,name):
		self.name = name
		Dog.counter += 1
	def bark(self):
		print "Wang!I m No.%d doge %s"%(Dog.counter,self.name)
if __name__=='__main__':
	dog = Dog("DouDou")
	dog.bark()