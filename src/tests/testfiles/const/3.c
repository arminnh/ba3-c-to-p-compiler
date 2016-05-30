int main() {
    int a = 5;
    const int* aa = &a;

    // assign const value to const variable, even though a is not const
    *aa = a;
}
