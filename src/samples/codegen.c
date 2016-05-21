int global_a = 5;
int global_b = 6;

void emptyReturn() {
    return;
}

int sum(int a, int b) {
    if (a == 2) {
        global_b = 10;
    }

    if (a == 1) {
        global_a = 50;
        return sum(2, 2);
    }
    return a+b;
}

int sum2() {
    int a, b;
    return sum(1, 2);
}


int summ(int b, int c, int d, int e) {
    return sum(b, sum(c, sum(d, e)));
}

int fac(int i) {
    if (i == 0) {
        return 1;
    }
    return fac(i-1) * i;
}

int fib(int a) {
    if (a == 0 || a == 1) {
      return 1;
    }

    return fib(a-1) + fib(a-2);
}fads

// int changeValue(int* a) {
//     *a = *a + 1;
//     return 0;
// }

int main() {
    int a = 2;
    // int *aa = &a;
    //
    // int* b = &a;
    // int** bb = &b;
    // int* cc = *bb;
    //
    // int c = *b;
    // int c_ = **bb;
    //
    // changeValue(&a);
    // &(*aa);
    // int *b = &(*aa);
    // // a = 2;
    // // a + 1;
    // // a = a + 6;
    //
    int b = 7;
    // //
    char c = 'a';
    //
    // a = a + b;
    //
    // b = sum(a, b);
    // emptyReturn();
    // a = b;
    // sum2();
    //
    // summ(1, a, b, 4);
    //
    // a = fac(2);
    // b = fib(2);
    // int d = a < b; //TODO: make this work

    a = 10;
    b = 5;
    while (b < a) {
      a = a - 1;
      if (c != '6') {
        a = a - 1;
      }
      else {
        b = b + 1;
      }
    }
    //
    // if (1 != 1) {
    //     10;
    // } else {
    //     20;
    // }
    //
    // if (2 == 2) {
    //     30;
    // }

    // a = 20;              // TODO: fix this, didnt work
    // while (a < 30) {     // TODO: fix this, didnt work
    //     a = a + 1;
    // }

    // a = a + 1;
    // -4;
    // +4;
    // 4 ==5;
    // a != 5;
    // 8 < 9 && 9 < 8;
    // 9 > 9 || 9 < 9;
    // ++a;
    // --a;
    // 3 * 8;
    // 7 / 3;
    // 4 - 5;
    // 3 * (4 + 5) / 7 * a;
    // a = (a = (a = 1));


    return 1;
}
