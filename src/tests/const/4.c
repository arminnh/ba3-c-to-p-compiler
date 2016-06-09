int main() {
    int a = 5;
    int* const aa = &a;
    *aa = 6; // should work
    *aa = *aa; // should work

    // assign pointer to const pointer
    aa = &a;
}
