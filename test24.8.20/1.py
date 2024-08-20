import random as rd
print("欢迎来到猜数游戏！")
def main():
    a=rd.randint(1,1000)
    x=1
    while(x<11):
        try:
            b=int(input("请输入一个1到1000的整数: "))
        except ValueError:
            print("格式错误！")
            x=x+1
            continue
        if (b>1000):
            print("范围1到1000！")
        else:
            if(a==b):
                print("恭喜！正确答案就是{}".format(a))
                x=x+1
                return
            if(a>b):
                if(x==10):
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
    print("蠢蛋！正确答案是{}".format(a))
if __name__=="__main__":
    main()                
