int a(int a) {
  return 0;
}

int b() {
  return 0;
}

int c(int a, float b) {
  return 0;
}

int d(int a, int b) {
  return 0;
}

int e(float a, float b) {
  return 0;
}

int f(int, int, float, float);

int g(char a, int b, float c, int* d, float** e) {
  return 0;
}

int main() {
  a(5490);
  b();
  c(5, 5e-36);
  d(3, 4);
  e(3.0, 7e-9);

  int* actual_int_p;
  int** i = &actual_int_p;

  float actual_float = 5.5;
  float* a = &actual_float;

  g('t', (4 - 3 + 5) % 2, *a, *i, &a);
}
