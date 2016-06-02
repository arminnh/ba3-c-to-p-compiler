#include <stdio.h>

int main() {
	//char hello[] = {'5'};
	char hello[6+5*8] = "hello";
	char* h = hello;

	char *s123 = h;
	hello = s123; // error

	char hello2[46];
	hello2 = hello; // error

	printf("%s\n", "hello");
	printf("%s\n", hello);
	printf("%s\n", h);

	printf("%s\n", &hello); // error
 }
