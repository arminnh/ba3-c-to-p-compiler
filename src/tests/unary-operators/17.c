#include <stdio.h>

int main() {
	int i = 6;
	const int* ii = &i;
	(*ii)++;
	void* const v = (void *) &i;
	v++, v--;
	printf("%i", *(int *) v);
}