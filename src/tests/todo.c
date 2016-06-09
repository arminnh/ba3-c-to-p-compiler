char b() { return 'a'; }
char a2() { return 'a'; }

int i() { return 2; }

int main() {
    int i[] = {1, 2, 3};

    // function a2() does not have same identifier as char a[]
    char a[] = {a2(), 'b', 'c'};

    // function b has same identifier as char b[]
    //      => error: called object 'b' is not a function or function pointer
    //      our error: function: undefined reference to 'b', is ok?
    char b[] = {b(), 'b', 'c'};

    return 0;
}
