# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:30:04 2024

@author: 26756
"""
import random as rd
def A():
    a=rd.randint(1,100)
    b=rd.randint(1,100)
    c=a+b
    print("{}+{}={}".format(a,b,c))
    
def main():
    A()
if __name__=="__main__":
    main()    