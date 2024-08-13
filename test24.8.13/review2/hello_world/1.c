#include<stdio.h>
extern int add (int x,int y);
int main()
{
    int a = 10;
    int b = 20;
    int sum = add(a,b);
    printf("%d",sum);
    return 0;
}