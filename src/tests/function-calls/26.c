#include <stdio.h>

int main() {
	printf("%5d\n", 5);
	printf("%5d\n", -5);
	printf("%5d\n", 19);
	printf("%5d\n", 350);
	printf("%5d\n", 4300);
	printf("%5d\n", -5400);
	printf("%5d\n", -64000);
	printf("%5d\n", 764000);
	printf("%5s\n", "he");
	printf("%d\n", 75);
	printf("%d\n", -75);
	printf("%5c\n", 'a');

	char string[3] = "he";
	printf("%5s\n", string);
	char string2[4] = "llo";
	printf("%5s\n", string2);
	printf("%s\n", string2);
	char string3[10] = "tootoolon";
	printf("%5s\n", string3);

	printf("%s\n", "hello");

	return 0;
}
