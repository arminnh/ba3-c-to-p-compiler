void nothing() {
	return 0;
}

void* nothing2() {
	void *a;
	return a;
}

int main() {
	int a1 = nothing();
	void a2 = nothing();
	void *a3 = nothing();
	void *a4 = nothing2();

	void a5, a6 = nothing();
	return 0;
}
