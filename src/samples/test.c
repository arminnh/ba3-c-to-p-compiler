#include <stdio.h>
#include <string.h>

int sum(int const * const * * a);
int sub(const int * const * * a);

int main() {
	//char hello[] = {'5'};
	char hello[6+5*8] = "hello", ccc = 'c', *str = "string", aaaa[] = "hier heb ik niet aan gedacht";

	int i = 5;
	int *arrint[1] = {&i};

	char* h = hello;
	h++;

	//int j = "hello"; // error

	*hello = 'u';
	// *hello = "uu"; // mag niet werken

	int const bb = 1;
	int bbb = 2;
	int const constarr[2] = {1, 2};
	// constarr[0] = bb; // TODO for extras: error: assignment of read-only location 'constarr[0]'


	// char* = char[]
	h = "newst";
	// h = 'n'; //error

	int *aaa;
	int aaaaa[] = {1, 2, 3};
	aaa = aaaaa;

	// printf("%s\n", hello);

	const int* p;
	// int* q = p; // TODO for extras: warning: initialization discards 'const' qualifier from pointer target type

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

	return 0;
}
