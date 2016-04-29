int f(char a, int b, float c, int* d, float** e, int f) {

}

int main() {
  int a;
  float* b;
  f('z', a, *b, &a, &b, b);
}
