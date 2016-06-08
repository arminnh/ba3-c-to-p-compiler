#include <stdio.h>

void matrixMultiply(int[10][10], int[10][10]);
int row1, row2, col1, col2;
int res[10][10];

int main() {

   int mat1[10][10], mat2[10][10], i, j, k;

   printf("Enter the row and column of first matrix: ");
   scanf("%d%d", &row1, &col1);
   printf("Enter the row and column of second matrix: ");
   scanf("%d%d", &row2, &col2);

   if (col1 != row2) {
      printf("Matrix multiplication is not possible");
   } else {
      printf("Enter the First matrix: ");
      for (i = 0; i < row1; i++) {
         for (j = 0; j < col1; j++) {
            scanf("%d", &mat1[i][j]);
         }
      }

      printf("Enter the Second matrix: ");
      for (i = 0; i < row2; i++) {
         for (j = 0; j < col2; j++) {
            scanf("%d", &mat2[i][j]);
         }
      }

      printf("\nThe First matrix is: n");
      for (i = 0; i < row1; i++) {
         printf("\n");
         for (j = 0; j < col1; j++) {
            printf("%d ", mat1[i][j]);
         }
      }

      printf("\nThe Second matrix is: n");
      for (i = 0; i < row2; i++) {
         printf("\n");
         for (j = 0; j < col2; j++) {
            printf("%d ", mat2[i][j]);
         }
      }
      matrixMultiply(mat1, mat2);
   }

   printf("\nThe multiplication of two matrixes is : \n");
   for (i = 0; i < row1; i++) {
      printf("\n");
      for (j = 0; j < col2; j++) {
         printf("%d ", res[i][j]);
      }
   }
   return 0;
}

void matrixMultiply(int a[10][10], int b[10][10]) {
   static int sum, i = 0, j = 0, k = 0;
   //row of first matrix
   if (i < row1) {
      //column of second matrix
      if (j < col2) {
         if (k < col1) {
            sum = sum + a[i][k] * b[k][j];
            k++;
            matrixMultiply(a, b);
         }
         res[i][j] = sum;
         sum = 0;
         k = 0;
         j++;
         matrixMultiply(a, b);
      }
      j = 0;
      i++;
      matrixMultiply(a, b);
   }
}
