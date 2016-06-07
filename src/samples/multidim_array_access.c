#include <stdio.h>

int f(int q[][3]) {
	return 0;
}

int main(void) {
	int arr[1][3];
	int i = 0, j = 1;
	arr[i][i] = 5;
	arr[i][j] = 6;
	arr[j][i] = 7;
	arr[j][j] = 8;

	int (*p)[2] = &arr[1];
	i = (*p)[0],
	j = (*p)[1],

	(*p)[0] = 16,
	(*p)[1] = 17;

	int (*q)[5][2];
	f(q);

	int arr2[5][6];
	for (int i = 0; i < 5; ++i)
		for (int j = 0; j < 5; ++j)
			arr2[i][j] = i + j;

	printf("print matrix\n");
	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j) {
			printf("%d", arr2[i][j]);
			if (j < 5 - 1) {
				printf(", ");
			}
		}
		printf("\n");
	}
}
