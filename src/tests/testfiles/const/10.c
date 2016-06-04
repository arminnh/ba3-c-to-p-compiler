int aaa(int a) {
	return 4;
}

int main() {
 	int const bb = 1;
 	int bbb = 2;
 	int const constarr[2] = {1, 2};

	constarr[0] = bb;
    int i = 4;
 	constarr[i] = bb;
 	constarr[aaa(5)] = bb;
	bb = 2;
}
