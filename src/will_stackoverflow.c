#include <stdio.h>

int f()
{
    return f();
}

int main()
{
    printf("Will overflow stack.\n");
    return f();
}
