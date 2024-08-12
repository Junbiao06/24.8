#include<stdio.h>
extern int add (int x,int y);
int main()
{
    int x = 100;
    int y = 200;
    int sum = add(x,y);
    printf("%d",sum);
    return 0;
}