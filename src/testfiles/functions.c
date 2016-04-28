int myFunction1(int const i, float *c) {
    if (i == 1)
        return 5;
        // return 5 * 3 * **c;
    else
        return 2*5;
}

int myFunction2(int i, float *c);

float myFunction3(int const i[5], int const j[]);

float myFunction4();

float myFunction3(int const i[5], int const j[]) {
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
    float e;
    const char f;

    // printf("%d\n", myFunction1(a, &e));
    // printf("%f\n", myFunction3(b, c));
    // printf("%f\n", myFunction3(h, c));
    // printf("%f\n", myFunction3(g, c)); // no error
    // printf("%f\n", myFunction3(i, c)); // no error
    // printf("%d\n", myFunction2(d, &e)); ERROR: undefined reference
    // myFunction6();
    // myFunction4();
    // TODO: dont raise undefined reference if function has been defined afterwards: first pass: check function definitions, second pass: check function calls with table from pass 1

    return 1;
}


int myFunction5();


int myFunction6() {
    // cannot include here
    // printf("hello world\n");
}

float myFunction4() {
    // printf("bla bla\n");
}
