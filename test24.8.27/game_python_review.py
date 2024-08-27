# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:29:45 2024

@author: 26756
"""

import random as rd
a=rd.randint(1,1000)
print("欢迎来到猜数游戏！")
def main():
    x=1
    while (x<11):
        try:
            b=int(input("请输入1到1000的数："))
        except ValueError:
            print("格式错误！")
            x=x+1
            continue
        if (a==b):
            print("回答正确！答案就是{}".format(a))
            return
        elif (a>b):
            print("小了！")            
            x=x+1
            continue
        elif (b>1000):
            print("范围1到1000！")
            x=x+1 
            continue
        else:
            print("大了！")
            x=x+1 
            continue
    print("菜鸡，答案是{}!".format(a))
    return        
if __name__=="__main__":
    main()        