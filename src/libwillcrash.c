#include <stdio.h>

#include "libwillcrash.h"

void *
call_me_back(callback_fn_t cb, void *data)
{
    void *res = cb(data);
    if (res)
    {
        puts("Impossible happened?");
    }
    return res;
}
