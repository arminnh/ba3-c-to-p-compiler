#include <stdio.h>
#include <stdbool.h>
#include "josse.h"
//#include "hello_world.c"

//int myFunction1(int i, float *c);
float myFunction2(const char c);

int myFunction1(int const i, float *c) {
    if (i == 1)
        return 5;
    else
        return 2*5;
}

int myFunction3(int const i[5], int const j[]) {
    return 1;
}

//int main(void)
int main(int argc, char *argv[])
{
    if (1)
        1 + 1; // declaration not allowed here in c99
    else
        2 + 2;

    if (0) {

    } else {

    }

    if (2 == 3) {
    } else if (2 == 2) {
        const int a[] = {1, 2, 3};
        int b = 0;
        b;
        1;
        b + 1;
    }
    int aaa = 2, ba = 3, ca[] = {1}, ad[5] = {1, 2, 3, 4, 5}, hh[5], *josse;
    while (0) {

    }

    do {

    } while (1 == 2);

    int const a = 5; //const must be initialized
    const int aa = 5;
    float b = 6, f = 7, g = 8;

    int c[5], cc[] = {1, 2}, dd[1] = {6};
    int const d[1+8+9] = {1, 2, 3};
    int e[7] = {1, 2}; // rest is 0

    myFunction1(a, &b);
    myFunction1(a, &g);

    return 1;
}
