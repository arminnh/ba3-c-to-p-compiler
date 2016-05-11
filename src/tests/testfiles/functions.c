int myFunction1(int const* i, float **c) {
    int *a;
    if (i == a)
        return 5 * 3 * **c;
    else
        return 2*5;
}

int myFunction2(int i, float *c);

const int myFunction3(int const i[5 + 6], int const j[]);

float myFunction4();

const int myFunction3(int const i[5], int const j[]) {
    if (i[3] == 0)
        return j[5];
    else  {
        return j[0];
    }
}

int sum(int const * const * * a);
int sub(const int * const * * a);


#include <stdio.h>
int main(void)
{
    const int a = 8, b[5] = {1, 2, 3, 4, 5}, c[6] = {7, 8};
    int d, g[8], h[5] = {}, i[2];
    float e, dd;
    const char f;

    const int * aPtr = &a;
    float * dPtr = &dd, ** dPtrPtr = &dPtr;

    myFunction1(&d, dPtrPtr);

    printf("aaa \n");
    printf("test %c, %f \n", '1', 1.0);
    printf("test %c, %5f \n", '2', 23.948984);
    printf("test %c, %i, %7f \n", '3', 528439789, 353332.53523);
    printf("test %37d, %c, %i, %5f \n", 1257, '4', 4, 4.9);
    printf("test %37d, %c, %i, %5f, %7s \n", 342347, '5', 4534, 4535.7, "oiejfoijfjeoairjeoi");

    e = myFunction4();
    // printf("%d\n", myFunction2(d, &e)); // undefined reference

    printf("%d\n", myFunction1(aPtr, dPtrPtr));
    printf("%i\n", myFunction3(b, c));
    printf("%i\n", myFunction3(h, c));
    printf("%i\n", myFunction3(g, c));
    printf("%i\n", myFunction3(i, c));
    myFunction6();

    return 1;
}


int myFunction5();


int myFunction6() {
    // cannot include here
    printf("hello world\n");
}

float myFunction4() {
    printf("bla bla\n");
}

int abc (int argc, char *argv[]) {

}
