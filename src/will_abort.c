#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

#define NLETTERS ('z'-'a'+1)

int a(char *s); int b(char *s); int c(char *s); int d(char *s);
int e(char *s); int f(char *s); int g(char *s); int h(char *s);
int i(char *s); int j(char *s); int k(char *s); int l(char *s);
int m(char *s); int n(char *s); int o(char *s); int p(char *s);
int q(char *s); int r(char *s); int s(char *s); int t(char *s);
int u(char *s); int v(char *s); int w(char *s); int x(char *s);
int y(char *s); int z(char *s);

int (*funs[])(char *s) = { a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z };

#define DISPATCH(s) do {                \
    if (*s == '\0')                     \
        abort();                        \
    int idx = abs((*s-'a') % NLETTERS); \
    return funs[idx](++s) + 1;          \
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

void print_help(void) {
    fprintf(stderr, "Usage: will_abort [--random|--stack <string>]\n");
    fprintf(stderr, "This program immediately abort()s.\n\n");
    fprintf(stderr, " --random          Crash with random (unique) stack.\n");
    fprintf(stderr, " --stack <string>  Crash with stack determined by <string>.\n\n");
}

int main(int argc, char *argv[]) {
    char arr[16];
    char *str;
    if (argc > 1) {
        if (0 == strcmp(argv[1], "--random")) {
            srandom(time(NULL));
            int i;
            for (i = 0; i < sizeof(arr)-1; i++) {
                arr[i] = (random() % NLETTERS) + 'a';
            }
            arr[sizeof(arr)-1] = '\0';
            str = arr;
        } else if (0 == strcmp(argv[1], "--help") || 0 == strcmp(argv[1], "-h")) {
            print_help();
            exit(EXIT_SUCCESS);
        } else if (0 == strcmp(argv[1], "--stack") && argc > 2) {
            str = argv[2];
        } else {
            print_help();
            exit(EXIT_FAILURE);
        }
        printf("Using string: %s\n", str);
    } else {
        str = "pampelmuse";
    }

    puts("Will abort.");
    return f(str);
}
