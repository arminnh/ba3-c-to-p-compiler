#include <stdio.h>

int main(void)
{
    printf("aaa \n");
    printf("test %c, %f \n", '1', 10);
    printf("test %c, %5f \n", 2, 23.948984);
    printf("test %c, %i, %7f \n", '3', "528439789", 353332.53523);
    printf("test %37d, %c, %i, %5f \n", 1257, '4', 4, 4.9);
    printf("test %37d, %c, %i, %5f, %7s \n", 342347, '5', 4534, 4535.7, "oiejfoijfjeoairjeoi");
    printf("%c%s%f%i%d%f%i%c%s", 'h', "ello", 314, 666, 42.0, 123.456, "789", '0', "1234565789");

    return 1;
}
