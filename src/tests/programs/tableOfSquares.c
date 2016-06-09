#include <stdio.h>

int main() {
    int n;

    printf("No\t Square\n");
    printf("-----------------\n");

    for (n = 1; n <= 10; n++) {
	   printf("%d\t%d\n", n, n * n);
   }
}
