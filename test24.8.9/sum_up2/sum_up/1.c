#include <stdio.h>
extern int Add (int x, int y);
int main()
{
    int a = 100;
    int b = 200;
    int sum = Add(a,b);
    printf("%d",sum);
    return 0;
}