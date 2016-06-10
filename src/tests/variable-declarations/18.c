\#include <stdio.h>

int main(void) {
    float a = {5.0};
    char b[] = {'a', 'b'};
    char bb[] = {};
    char bbb = 'd';
    char bla[] = "anblea";
    // char * = char []
    char *blab = "anblea";
    // char ** = char **
    char **blabl = &blab;
    // char *** = char ***
    char ***blabla = &blabl;

    return 0;
}
