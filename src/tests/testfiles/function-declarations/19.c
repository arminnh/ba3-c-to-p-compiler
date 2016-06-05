void sum(int a, int b) {
	return 'a';
}

void* sub(int a, int *b) {
	return (void *) b;
}

void nothing();

void nothing() {
	return 0;
}

void nothing();

int main() {
	sum(1, 2);
	int a = sum(1, 2);

	int *b = &a;
	void *c = sub(1, b);

	return 0.0;
}
