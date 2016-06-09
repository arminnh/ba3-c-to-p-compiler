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

	int (*p)[2] = &arr[5];
	i = (*p)[0],
	j = (*p)[1],

	(*p)[0] = 16,
	(*p)[1] = 17;

	int (*q)[5][2];
	f(q);

	int *(*r[4][5])[8] = &arr[6];
	r = &p[4];
}
