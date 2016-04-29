#include <stdio.h>
#include <stdbool.h>

// #include "josse.h"
// #include "armin.h"


int sum(int a, int b) {
    return a + b;
}

int sum(int aaa, int bbb);
int sum(int aaaa, int);

int sub(int, int);


int sub(int a, int b) {
    return a;
}

int fun1(int const * const * * a);
int fun2(const int * const * * a);

int main(int argc, char *argv[])
{
    int a = 1;
    while (a != 3) {
        a = sum(a = 2, 1);
    }

    sub(5, 6);

    if (a != 3 && 1) {
        a;
    } else {
        a == 3;
    }

    int b = 0;
    b;

    float c[2] = {1.1, 2.2};
    (1 || 2 ? c[0] : c[1]);

    return 1;
}
