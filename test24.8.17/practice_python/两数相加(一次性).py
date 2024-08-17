# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 09:50:28 2024

@author: 26756
"""
53
def A():
    try:
        a,b=map(int,input("Please input 2 integers: ").split())
    except ValueError:
        return("input error...")
    c=a+b
    d=("{}+{}={}".format(a,b,c))
    return(d)
def main():
    d=A()
    print(d)
    
if __name__=="__main__":
    main()    