int f(char a, int b, float c, int* d, float** e, int f) {
  return 0;
}

int main() {
  int a;
  float* b;
  f('z', a, *b, &a, &b, b);
}
