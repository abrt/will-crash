#include <stdio.h>

__attribute__((optimize((0))))
__attribute__((optnone))
int f()
{
    return f();
}

int main()
{
    printf("Will overflow stack.\n");
    return f();
}
