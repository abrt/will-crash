#include <stdio.h>
#include <stdarg.h>
#include <string.h>

#include <link.h>

#include "libwillcrash.h"

static void crash(int *p) __attribute__ ((noinline));
void varargs(size_t num_args, ...) __attribute__ ((noinline, noclone));
static inline void inlined(int *p) __attribute__ ((always_inline));
void f(int *p) __attribute__ ((noinline));
static void *callback(void *data) __attribute__ ((noinline));
void recursive(int i) __attribute__ ((noinline));

void crash(int *p)
{
    puts("Will segfault.");
    int i = *p;
    printf("Result: %d\n", i);
}

void varargs(size_t num_args, ...)
{
    va_list ap;
    va_start(ap, num_args);
    for (; num_args > 0; num_args--)
    {
        int *p = va_arg(ap, int *);
        if (!p)
        {
            crash(p);
        }
    }
    va_end(ap);
}

void inlined(int *p)
{
    int num = 42;
    varargs(2, &num, p);
}

void f(int *p)
{
    inlined(p);
}

void *callback(void *data)
{
    f((int*)data);

    return NULL;
}

void recursive(int i)
{
    if (i <= 0)
    {
        void *p = call_me_back(callback, NULL);
        if (p)
        {
            puts("No idea what I'm doing.");
        }
    }
    else
        recursive(i-1);
}

static void break_link_map()
{
    puts("Overwriting link_map.");
    _r_debug.r_map->l_next = (struct link_map *)0x1337BEEF;
    _r_debug.r_map->l_name = "invalid";
}

int main(int argc, char *argv[])
{
    if (argc >= 2 && 0 == strcmp(argv[1], "--break-link-map"))
    {
        break_link_map();
    }

    recursive(2);
    return 0;
}
