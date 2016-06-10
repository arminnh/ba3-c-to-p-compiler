#include <stdio.h>

int global_a = 5;
int global_b = 6;

int sum(int a, int b) {
    if (a == 2) {
        global_b = 10;
    }

    if (a == 1) {
        global_a = 50;
        return sum(2, 2);
    }
    return a+b;
}


int main() {
    printf("globals: %i and %i \n", (global_a, global_b, global_a, global_b, global_a, global_b, global_a), global_b);

    global_a = 1, global_b = 2, printf("globals: %i and %i \n", (global_a, global_b, global_a, global_b, global_a), (global_b, global_a, global_b));

    sum(2, 111), printf("globals: %i and %i \n", (global_a, global_b, global_a), (global_b, global_a, global_b, global_a, global_b)); 

    sum(1, 1), printf("globals: %i and %i \n", global_a, (global_b, global_a, global_b, global_a, global_b, global_a, global_b));

    return 0;
}
