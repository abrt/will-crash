#include<stdio.h>

int main() {
    puts("Will segfault.");
    int i = *(int*)0;
    return i;
}
