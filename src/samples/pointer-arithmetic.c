#include <stdio.h>

int main() {
	int i[3];
	int* ii;

	for (int j = 0; j < 3; ++j) {
		i[j] = j + 1;
	}

	i[0] = 1, i[1] = 2, i[2] = 3;

	ii = i;

	for (int j = 0; j < 3; ++j) {
		printf("%d\n", i[j]);
	}

	for (int j = 0; j < 3; ++j) {
		*ii = *ii + j + 1;
		ii = ii + 1;
	}

	for (int j = 0; j < 3; ++j) {
		printf("%d\n", i[j]);
	}

	int k[2][2];
	k[0][0] = 5;
	k[1][0] = 6;

	int (*kk)[2] = k;

	printf("%d\n", (*kk)[0]);

	kk = 1 + kk;

	printf("%d\n", (*kk)[0]);

	kk = kk -1;

	printf("%d\n", (*kk)[0]);

	kk = kk - (-1);

	printf("%d", (*kk)[0]);

	0;

	return 0;
}
