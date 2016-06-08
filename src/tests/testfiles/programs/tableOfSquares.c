#include <stdio.h>

void main() {
    int n;
    printf("No\t Square\n");
    printf("-----------------n");
    for (n = 1; n <= 10; n++)
	printf("%d\t%dn", n, n * n);
}
