int main(void) {
	int arr[1][3];
	int (* const(* const arr2)[4][2])[][] = &arr;
	int (* const(* const arr3)[4][2])[][3] = &arr;
}
