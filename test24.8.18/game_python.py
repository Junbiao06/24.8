import random as rd
print("欢迎来到猜数游戏！")
def main():
    a=rd.randint(1,100)
    x=1
    while (x<11):
        try:
            b=int(input("输入整数(1~100): "))
        except ValueError:
             print("格式错误！")
             x=x+1
             continue
        if (b>100):
            print("范围1~100!")
            x=x+1
            continue
        else:
            if (a==b):
                print("恭喜！答案就是{}".format(a))
                return
            elif(a>b):
                print("太小了！")
                x=x+1
                continue
            else:
                print("太大了！")
                x=x+1
                continue
    print("太蠢了，正确答案是{}".format(a))
if __name__=="__main__":
    main()
