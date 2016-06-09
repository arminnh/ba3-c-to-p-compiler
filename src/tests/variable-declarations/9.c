int main(void) {
    char hello[6+5*8] = "hello";

    *hello = 'u';
    *hello = "uu"; // error
    return 0;
}
