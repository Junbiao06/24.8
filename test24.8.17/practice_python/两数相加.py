# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:07:00 2024

@author: 26756
"""

def A():
    x="yes"
    while(x=="yes"):
        try:
            a,b=map(int,input("Please input 2 integers: ").split())
        except ValueError:
            print("input error...")
            continue
        c=a+b
        print("{}+{}={}".format(a,b,c))
        x=input("Continue?yes&no: ")
    return

def main():
    A()
    
if __name__=="__main__":
    main()    