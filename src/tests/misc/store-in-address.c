#include <stdio.h>

int main() {
    int a, b = 5;
    int *aa = &a, *bb = &b;

    // loads b (= 5) on address 12
    *((int*) 12) = b;
}
