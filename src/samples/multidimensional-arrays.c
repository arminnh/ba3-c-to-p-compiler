#include <stdio.h>

int main() {
  const int twee = 2;
  const int a[][2][2] = {
    {
      {10, 11}, {12, 13}
    },
    {
      {14, 15}, {16, 17}
    }
  };

  const int arr[] = {10, 20, 30};

  printf("%i\n", *(**a + 1));
  printf("%i\n", a[0][1][0]);
  printf("%i\n", *(arr+1) + 1);


  int n = 5;
  int arr2[n];

  int a2[5][10] = {
    { 0, 1, 2 },
    { 0, 1, 2 },
    { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
    { 0, 0, 0, 0, 0, 0, 7, 0, 0, 0 },
    { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }
  };

  // int *a3 = a[2];

  printf("%i, %i\n", a2[1][2], a2[3][6]);

}
