# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:51:18 2024

@author: 26756
"""

import random as rd
def A():
    a=rd.randint(1,100)
    count=1
    while(count<6):
        try:
            b=int(input("Please input a integer ranging from 1 to 100: "))
        except ValueError:
            print("Please input a integer ranging from 1 to 100!!!")
            count=count+1
            continue
        if(b>100):
            print("Please input a integer ranging from 1 to 100!!!")
            count=count+1
            continue
        else:
            if(a==b):
                print("Congratulations!!")
                break
            elif(a>b):
                print("Too small...")
                count=count+1
                continue
            else:
                print("Too big...")
                count=count+1
                continue
    print("you are stupid...The number is {}!!!".format(a))
def main():
    A()
if __name__=="__main__":
    main()        
        