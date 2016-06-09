#include <stdio.h>

int fact(int);

int main() {
   int factorial, num;

   printf("Enter the value of num :");
   scanf("%d", &num);

   factorial = fact(num);
   printf("Factorial is %d", factorial);

   return (0);
}

int fact(int n) {
   if (n == 0) {
      return (1);
   }
   return (n * fact(n - 1));
}
