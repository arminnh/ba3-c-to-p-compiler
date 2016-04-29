int main(int argc, char *argv[])
{
    int a = 5, b, c;

    if (1)
        1 + 1; // declaration not allowed here in c99
    else
        2 + 2;

    if (1)
        1;

    if (0 || 1) ;
    else ;

    if (0 && 1) {
        a;
    } else {
        if (0) {
            b;
        } else {
            if (1) {
                c;
                int a;
            }
        }
    }

    if (2 == 3) {
    } else if (2 == 2) {
        const int a[] = {1, 2, 3};
        int b = 0;
        b + 1;
    }

    while (0) {
        1 + 1;
    }

    do {
        c = a + b;
        int var;
    } while (1 == 2);

    return 1;
}
