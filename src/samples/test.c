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
	// constarr[0] = bb; // error


	// char* = char[]
	h = "newst";
	// h = 'n'; //error

	int *aaa;
	int aaaaa[] = {1, 2, 3};
	aaa = aaaaa;

	// printf("%s\n", hello);

	const int* p;
	// int* q = p; // error

	const int a, *b, * const c;
	int const aa, *ab, * const ac;
	int const * const * abab, *aab, * const caa;

	// char (*acec[5])[]; // TODO: special case
	// char cPtr = *c;

	return 0;
}
