#include <stdio.h>

int sum(int a, int b) {
    return a + b;
}

float sumf(float a, float b) {
    return a + b;
}

char sumc(char a, char b) {
    return a;
}

char* sums(char* a, char* b) {
    return b;
}

int main(void)
{
    int a = 1, b = 2;
    float c = 1.1, h = 2.2;
    char d = 'd', e = 'e';
    char* f = "hello", i[] = "world";

    printf("aaa \n");
    printf("test %c, %f \n", d, a);
    printf("test %c, %5f \n", h,  h);
    printf("test %c, %i, %7f \n", e, e, h);
    printf("test %37d, %c, %i, %5f \n", sumc(d, e), sumc(d, 'd'), a, sumf(1.0, h));
    printf("test %37d, %c, %i, %5f, %7s \n", a, sum(1, b), b, h, f);
    printf("%c%s%f%i%d%f%i%c%s \n", 'h', sumf(c, h), b, b, h, sums(f, f), sum(a, b), f, sums("hello", i));
    printf("%s\n", i);

    return 1;
}
