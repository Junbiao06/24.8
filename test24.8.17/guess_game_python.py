# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:07:56 2024

@author: 26756
"""

import random as rd
def A():
    x=1
    a=rd.randint(1,100)
    print("欢迎来到猜数游戏！只有8次计划喔。")
    while (x<9):
        try:
            b=int(input("输入一个整数(范围1~100): "))
        except ValueError:
            print("格式错误！")
            x=x+1
            continue
        if (b>100):
            print("范围1~100！！")
        else:
            if (a==b):
                print("答对了！就是{}！".format(a))
                break  #终止循环，跳出循环
            elif (a>b):
                print("太小了！")
                x=x+1
                continue
            else:
                print("太大了!")
                x=x+1
                continue
    if(x==10):
        print("笨蛋！正确数字是{}".format(a))
        return
    
def main():
    A()
if __name__=="__main__":
    main()    
                