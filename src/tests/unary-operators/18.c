int main() {
	const int i;
	+i; // check that unary + and - don't check const compatibility
	-i;
}