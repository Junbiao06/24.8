# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:46:49 2024

@author: 26756
"""

def A():
    x="yes"
    while (x=="yes"):
        try:
            a,b=map(int,input("Please input 2 integers: ").split())
        except ValueError:
            return("input error...")
            continue
        c=a+b
        d=("{}+{}={}".format(a,b,c))
        print(d)
        x=input("Continue?yes&no:")
    return

def main():
    A()
if __name__=="__main__":
    main()    