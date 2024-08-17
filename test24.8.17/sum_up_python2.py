# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:21:45 2024

@author: 26756
"""

C=range(101)
try:
    A,B=map(int,input("Please input 2 integers: ").split())
except ValueError:
    print("input error...")
    A=-1
    B=-1
while A not in C or B not in C:
#while A>100 or A<0 or B>100 or B<0:
    try:
        A,B=map(int,input("Please input 2 integers: ").split())
    except ValueError:
        print("input error...")
input("{}+{}={}".format(A,B,A+B))