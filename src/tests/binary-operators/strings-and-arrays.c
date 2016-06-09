#include <stdio.h>

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
    // char * = char []
    **blabla = "a";
    // char * = char []
    blab = "a";
    // char * ++
    blab++;
    // char * = char []
    // blab = 34.05; // error: incompatible types when assigning to type 'char *' from type 'double'
    blab = "B";

    // int *asssds = {1, 2}; // warning: initialization makes pointer from integer without a cast [enabled by default]
    // ^^^ plus -> warning: excess elements in scalar initializer [enabled by default]

    // int [] = int []
    int aaa[] = {1, 2, 3, 4, 5};
    int aaaa[] = {1, 2};
    // int * = int []
    int *asssds = aaa;
    asssds = aaaa;

    const int length = 1;
    float ffl = 5.0;
    float fff[2];
    fff[0] = ffl;
    fff[1] = ffl - 1.0;
    fff[2] = ffl + 1.0;

    // float * = float []
    float *fltPtr = fff;

    float fltArr[] = {1.0, 2.0, 3.0};
    fltPtr = fltArr;

    // int *integerPtr = {1, 2, 3}; // warning: initialization makes pointer from integer without a cast [enabled by default]

    // in general: TYPE * = TYPE []   ->  is ok

    return 0;
}
