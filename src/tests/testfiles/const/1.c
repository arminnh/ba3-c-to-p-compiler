int main() {
    int a = 5;
    const int b = a + 2;

    // assign non-const value to non-const variable
    a = 6;

    // assign const value to non-const variable
    a = b;

    const int* aa = &a;
    // assign const value to non-const variable
    a = *aa;

    int* const aaa = &a;
    // assign const value to non-const variable
    aa = aaa;
    // assign value to const pointer
    *aaa = b;
}
