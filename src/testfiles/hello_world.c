#include <stdio.h>
#include <stdbool.h>

#include "josse.h"
#include "armin.h"


//int b = 5;

int sum(int a, int *b) {
    return a + b;
}

int sum(int aaa, int *bbb);
int sum(int aaaa, int*);

int sub(int, int);

//int sum;

int sub(int a, int b) {
    return a;
}

int main(int argc, char *argv[])
{
    int* a = 1;
    while (a != 3) {
        a = sum(a = 2, 1);
    }

    sub(5, 6);

    if (a != 3 && 1) {
        // printf("a == %d\n", a);
    } else {
        // printf("a == 3\n");
    }

    // printf("b == %d\n", b);
    int b = 0;
    // printf("b == %d\n", b);

    float c[2] = {1.1, 2.2};
    //printf("%f\n", (1 || 2 ? c[0] : c[1]));

    return 1;
}

// int abc (int argc, char *argv[]) { } //not recognized by grammar