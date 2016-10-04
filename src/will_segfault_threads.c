#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
#include <stdlib.h>

pthread_t tid[2];

#define NLETTERS ('z'-'a'+1)

int a(char *s); int b(char *s); int c(char *s); int d(char *s);
int e(char *s); int f(char *s); int g(char *s); int h(char *s);
int i(char *s); int j(char *s); int k(char *s); int l(char *s);
int m(char *s); int n(char *s); int o(char *s); int p(char *s);
int q(char *s); int r(char *s); int s(char *s); int t(char *s);
int u(char *s); int v(char *s); int w(char *s); int x(char *s);
int y(char *s); int z(char *s);

int (*funs[])(char *s) = { a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z };

#define DISPATCH(s) do {                     \
    if (*s == '\0')                          \
        fprintf(NULL, "I am about to die!"); \
    int idx = abs((*s-'a') % NLETTERS);      \
    return funs[idx](++s) + 1;               \
} while(0)

int a(char *s) { DISPATCH(s); } int b(char *s) { DISPATCH(s); } int c(char *s) { DISPATCH(s); }
int d(char *s) { DISPATCH(s); } int e(char *s) { DISPATCH(s); } int f(char *s) { DISPATCH(s); }
int g(char *s) { DISPATCH(s); } int h(char *s) { DISPATCH(s); } int i(char *s) { DISPATCH(s); }
int j(char *s) { DISPATCH(s); } int k(char *s) { DISPATCH(s); } int l(char *s) { DISPATCH(s); }
int m(char *s) { DISPATCH(s); } int n(char *s) { DISPATCH(s); } int o(char *s) { DISPATCH(s); }
int p(char *s) { DISPATCH(s); } int q(char *s) { DISPATCH(s); } int r(char *s) { DISPATCH(s); }
int s(char *s) { DISPATCH(s); } int t(char *s) { DISPATCH(s); } int u(char *s) { DISPATCH(s); }
int v(char *s) { DISPATCH(s); } int w(char *s) { DISPATCH(s); } int x(char *s) { DISPATCH(s); }
int y(char *s) { DISPATCH(s); }
int z(char *s) { DISPATCH(s); }


void *doSomeThing(){
    char arr[16];
    char *str;
    srandom(time(NULL));
    int i;
    for (i = 0; i < sizeof(arr) -1; i++) {
        arr[i] = (random() % NLETTERS) + 'a';
    }
    arr[sizeof(arr)-1] = '\0';
    str = arr;
    f(str);
}


int main(void){
    int i = 0;
    int err;

    while(i < 2){
        err = pthread_create(&(tid[i]), NULL, &doSomeThing, NULL);
        if (err != 0)
            printf("\nCan't create thread :[%s]", strerror(err));
        else
            printf("\nThread created successfully\n");
        i++;
    }
    while(1);
    return 0;
}
