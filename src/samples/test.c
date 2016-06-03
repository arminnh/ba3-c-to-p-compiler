#include <stdio.h>
#include <string.h>

int* f(int i) {
	return (int *) 0;
}

int main() {
	// int **cc;
	int aa[1][2][3][4][5][6];
	// cc = aa;

	// char a;
	printf("%s\n", aa);
	int i = aa;
	f(aa);
 }
