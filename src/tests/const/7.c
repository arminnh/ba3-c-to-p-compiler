int main() {
    int a = -5;
    int* aa = &a;
    int* const * aaa = &aa;
    int** intarray[] = {aaa};
}
