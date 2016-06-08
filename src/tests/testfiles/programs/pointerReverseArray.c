#include<stdio.h>

int main() {
   int size, i, arr[30];
   int *ptr;

   ptr = &arr[0];

   printf("\nEnter the size of array : ");
   scanf("%d", &size);

   printf("\nEnter %d integers into array: ", size);
   for (i = 0; i < size; i++) {
      scanf("%d", ptr);
      ptr++;
   }

   ptr = &arr[size - 1];

   printf("Elements of array in reverse order are :\n");
   for (i = size - 1; i >= 0; i--) {
      printf("  Element %d is %d \n", i, *ptr);
      ptr--;
   }
}
