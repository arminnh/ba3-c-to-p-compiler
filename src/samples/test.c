#include <stdio.h>
#include <string.h>

int aaaa(const const  const  const dwdwa) {
	return 4;
}

int sum2() {
    // int int float a;

    // return (void) a;
}

void sum3() {
    return;
}

int f2(int i) {
	return 1;
}

int sum(int const * const * * a);
int sub(const int * const * * a);

int* f(int i) {
	return (int *) 0;
}

int main() {
	// int **cc;
	int (*zz[1][2])[][5][5][6];
	// cc = aa;

	// char a;
	// printf("%s\n", zz);
	// int i = zz;
	// f(zz);

	//char hello[] = {'5'};
	char hello[6] = "hello", ccc = 'c', *str = "string", aaaa[] = "hier heb ik niet aan gedacht";

	int i = 5;
	int *arrint[1] = {&i};

	char* h = hello;
	h++;

	//int j = "hello"; // error

	*hello = 'u';
	// *hello = "uu"; // mag niet werken

	int const bb = 1;
	int bbb = 2;
	// int const constarr[2] = {1, 2};
	// constarr[0] = bb;
	// constarr[i] = bb;
	// constarr[aaa(5)] = bb;
	// bb = 2;


	// char* = char[]
	h = "newst";
	// h = 'n'; //error

	int *aaa;
	int aaaaa[] = {1, 2, 3};
	aaa = aaaaa;

	// printf("%s\n", hello);

	const int* p;
	// int* q = p;

	const int a, *b, * const c;
	int const aa, *ab, * const ac;
	int const * const * abab, *aab, * const caa;

	/*char *y[5][6];
	char (*y2)[5][4];
	char *(y3[5])[4];
	char ((((*((y4[5]))))[4]));*/

	char y5[5];
	char (y6)[5];
	char (y7[5]);
	char ((((((y8[5]))))));
	char (y9)[5];
	int (abla) = 5, blabla = 3, ((ablaba)[3]) = {1, 2, 3};

	char *y[5];
	char (*y2)[5];
	char *(y3[5]);
	char ((((*((y4[5]))))));
	char *(*y10[4]);

	// int a123[] = {5, 6};
	// int a234[2];
	// a234 = a123;
	// int *a345 = a123;
	// a123 = a345;
	//
	// char *s123 = h;
	// hello = s123;
	//
	// char hello2[46];
	// hello2 = hello;
	//
	//
	// printf("%s\n", "hello");
	// printf("%s\n", hello);
	// printf("%s\n", &hello);
	// printf("%s\n", h);

	char format[50] = "blabla \n %s \n %i \n  blabla \n";
	format[0] = 'z';
	format[1] = 'z';
	format[2] = 'z';
	format[3] = 'z';
	format[4] = 'z';
	format[5] = 'z';
	// printf(format, "5");


    char *testS[] = {"hello", "world"};

	int arr[1][3];
	int (* const(* const arr2)[4][2])[][] = &arr;
	int (* const(* const arr3)[4][2])[][3] = &arr;
 }
