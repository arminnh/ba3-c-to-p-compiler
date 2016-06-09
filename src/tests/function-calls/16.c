
int f(char string[]) {
  return (int) string[0];
}

int main() {
  int* aa;
  // int a[5] = aa;
  char string[] = "hello";
  char string2[] = "world";

  char *s3 = string;
  char string3[] = s3;

  char string4[] = string;

  int a = 5;
  int *aPtr = &a;
  int arr[] = aPtr;
  // string = string2;
  f(string);
}
