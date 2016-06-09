#include <stdio.h>

int main() {

    int a = 1, b = 2;
    char * world = "world";

    printf("%s\n", "hello", "world");
    printf("%s %d %i %s\n", "hello", a, b, "world", 1, 2, 3);

    printf("%i %d %i\n", a, b);
    printf("%s\n");

    return 0;
}
