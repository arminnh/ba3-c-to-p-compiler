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

	//int j = "hello";

	/*char hello2[strlen(hello)];
	memcpy(hello2, hello, strlen(hello));*/

	*hello = 'u';
	// *hello = "uu"; // mag niet werken

	int const bb = 1;
	int bbb = 2;
	int const constarr[2] = {1, 2};
	constarr[0] = bb;

	//hello;

	// char* = char[]
	h = "newst";
	// h = 'n';

	int *aaa;
	int aaaaa[] = {1, 2, 3};
	aaa = aaaaa;

	// printf("%s\n", hello);

	// const int* p;
	// int* q = p;

	// const int a, *b, * const c;
	// int const a, *b, * const c;
	// int const * const *  a, *b, * const c;

	// char (*c[5])[]; // special case
	// char *cPtr = &c;

	return 0;
}