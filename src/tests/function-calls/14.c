#include <stdio.h>

int main(void)
{
    int a = 1;
    float b = 2.0;
    char* f = "hello";

    printf(a);
    printf(a, b, f);

    return 1;
}
