#include <stdio.h>

int main(void) {
	int arr2[15][16];
	for (int i = 0; i < 15; ++i)
		for (int j = 0; j < 16; ++j)
			arr2[i][j] = i + j;

    printf("[\n");
	for (int i = 0; i < 15; ++i) {
        printf("  [ ");
		for (int j = 0; j < 16; ++j) {
			printf("%2d", arr2[i][j]);
			if (j < 16 - 1) {
				printf(", ");
			}
		}
		printf(" ],\n");
	}
    printf("]\n");
}
