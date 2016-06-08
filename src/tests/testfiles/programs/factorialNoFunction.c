#include <stdio.h>

void main() {
    int i, number, factorial = 1;

    printf("\nEnter the number : ");
    scanf("%d", &number);

    for (i = 1; i <= number; i++)
	   factorial = factorial * i;

    printf("\nFactorial of %d is %d", number, factorial);
}
