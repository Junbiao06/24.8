#include <stdio.h>
extern int add (int x, int y);
int main()
{
    int a = 555;
    int b = 555;
    int sum = add(a,b);
    printf("%d",sum);
    return 0;
}