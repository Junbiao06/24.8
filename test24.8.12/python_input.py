# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:46:45 2024

@author: 26756
"""

#A=input("Please input a integer: ")
#print (A)


B,C,D=(input("please input 3 integers: ").split()) #均为列表
print(B,C,D)
print(type(B))


E,F,G,H=map(int,input("Please input 4 integers: ").split())
print(E,F,G,H)
print(type(E))


I=input("input somethings: ").split() #可以输入不同数据类型
for x in I:
    print(I)
    print(type(I))