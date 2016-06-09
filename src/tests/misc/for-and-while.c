#include <stdio.h>

void f(int i) {

}

int main() {
	for (int i = 5, j = 5; i < 30; ++i) {
		for (int i = 5;; ++i) {
			if (i >= 7) {
				break;
			}
		}
		if (i >= 25) {
			break;
		}
	}

	int i = 0;

	while (i < 30) {
		++i;
		printf("i = %d\n", i);
	}

	do {
		i++;
		printf("i = %d\n", i);
	} while (i < 35);

	return 0;
}
