int main(void) {
    char hello[6+5*8] = "hello";
    char* h = hello;
    h++;

    *hello = 'u';

    int const bb = 1;
    int bbb = 2;
    int const constarr[2] = {1, 2};

    // char* = char[]
    h = "newst";

    // char* = char
    h = 'n'; //error
    h = 8; // error

    h = "no error";

    return 0;
}
