#include <stdio.h>

int fib(int a) {
    if (a == 0 || a == 1) {
      return 1;
    }

    return fib(a-1) + fib(a-2);
}

int main() {
    printf("fib of 1: %i\n", fib(1));
    printf("fib of 2: %i\n", fib(2));
    printf("fib of 3: %i\n", fib(3));
    printf("fib of 4: %i\n", fib(4));
    printf("fib of 5: %i\n", fib(5));
    printf("fib of 6: %i\n", fib(6));

    return 0;
}
