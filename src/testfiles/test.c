#include <stdio.h>
#include <string.h>

int sum(int const * const * * a);
int sub(const int * const * * a);

int main() {
	//char hello[] = {'5'};
	char hello[6+5*8] = "hello", ccc = 'c', *str = "string";
	
	int i = 5;
	int *arrint[1] = {&i};

	char* h = hello;
	h++;

	/*char hello2[strlen(hello)];
	memcpy(hello2, hello, strlen(hello));*/

	*hello = 'u';

	hello;

	h = "newst";

	printf("%s\n", hello);

	const int* p;
	int* q = p;

	const int a, *b, * const c;
	int const a, *b, * const c;
	int const * const *  a, *b, * const c;

	return 0;
}