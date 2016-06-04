int main() {
	for (int i = 5, j = 5; i < 10; ++i) {
		if (j > 6) {
			continue;
		}
		++j;
	}

	while (1) {
		break;
	}

	return 0;
}