#include <stdio.h>

int main(void)
{
    int a = 1;
    float b = 2.0;
    char* f = "hello";

    printf("%v\n", a);
    printf("%y, %l, %z\n", a, b, f);

    return 1;
}
