# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import random as rd
print("欢迎来到猜数游戏！")
def main():
    a=rd.randint(1,1000)
    x=1
    while (x<11):
        try:
            b=int(input("请输入1到1000之间的数： "))
        except ValueError:
            print("格式错误！")
            x=x+1 
            continue
        if (b>1000):
            print("范围1到1000！")
        else:
            if (a==b):
                print("恭喜!正确答案就是{}!".format(a))
                return
            elif (a>b):
                if (x==10):
                    break
                else:
                    print("小了！")
                    x=x+1
                    continue
            else:
                if(x==10):
                    break
                else:
                    print("大了！")
                    x=x+1 
                    continue
    print("蠢蛋！答案是{}!".format(a))      
    return
if __name__=="__main__":
    main()      