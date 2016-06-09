int f(int a) {
  return 0;
}

void f2(int a) {
    return;
}

int main() {
    int a = 5;

    a = f(a) + (f2(a) * (f(a) - (f2(a) / f(a)) * (f2(a) + f(a)) / f2(a) % f(a) % f2(a)));
    a = f(a) ? (f2(a) && (f(a) > (f2(a) / f(a)) || (f2(a) + f(a)) / f2(a) % f(a) < f2(a))) : (f2(5));

    return 0;
}
