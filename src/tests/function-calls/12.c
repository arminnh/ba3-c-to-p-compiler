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
    char f[] = "hello", i[] = "world";

    printf("aaa \n");
    printf("test %c, %f \n", d, c);
    printf("test %c, %5f \n", e,  h);
    printf("test %c, %i, %7f \n", e, b, h);
    printf("test %37d, %c, %i, %5f \n", sum(1, b), sumc(d, 'd'), a, sumf(1.0, h));
    printf("test %37d, %c, %i, %5f, %7s \n", a, sumc(d, e), b, h, f);
    printf("%c%s%f%i%d%f%i%c%s \n", 'h', sums(f, f), c, b, a, sumf(c, h), sum(a, b), d, sums("hello", i));
    printf("%s\n", i);

    return 1;
}
