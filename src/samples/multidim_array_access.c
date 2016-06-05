

int main(void) {
	int arr[2][2];
	int i = 0, j = 1;
	arr[i][i] = 5;
	arr[i][j] = 6;
	arr[j][i] = 7;
	arr[j][j] = 8;

	 // TODO: this sort of assignment should give an 'incompatible pointer types' error
	// if number of elements in array pointed to does not match, see gcc 
	int (*p)[2] = &arr[j];
	i = (*p)[0];
	j = (*p)[1];

	(*p)[0] = 16;
	(*p)[1] = 17;

	// int arr2[5];
	// arr2[4];
}