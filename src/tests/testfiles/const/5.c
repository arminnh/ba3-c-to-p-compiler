int main() {
    int a = 5;
    const int* const aa = &a;

    aa = &a;
    *aa = a;
}
