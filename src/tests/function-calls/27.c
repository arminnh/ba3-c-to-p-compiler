#include <stdio.h>

int main() {
	char string1[30], string2[30], string3[30];

	printf("Enter 3 strings consecutively, with ^[ in between.\n");
	scanf("%s%s%s", string1, string2, string3);

	printf("The 3 strings were:\n%s\n%s\n%s\n", string1, string2, string3);
}