#include <stdio.h>
extern int Add (int x, int y);
int main()
{
    int a = 9;
    int b = 70;
    int sum = Add(a,b);
        printf("%d",sum);
        return 0;
}