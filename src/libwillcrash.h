typedef void* (*callback_fn_t)(void *);

void *
call_me_back(callback_fn_t cb, void *data);
