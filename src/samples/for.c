
void f(int i) {

}

int main() {
	for (int i = 5, j = 5; i < 30; ++i) {
		if (j > 6) {
			continue;
		}
		++j;
	}

	int i = 0;

	while (i < 30) {
		++i;
	}

	return 0;
}
