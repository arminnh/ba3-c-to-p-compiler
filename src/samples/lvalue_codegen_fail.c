#include <stdio.h>

int main() {
    int a, b = 5;
    int *aa = &a, *bb = &b;

    *((int*) 12) = b;

}
