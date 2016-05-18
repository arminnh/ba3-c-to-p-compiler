// int sum(int a, int b) {
//     return a+b;
// }
//
// int summ(int b, int c, int d, int e) {
//     return sum(b, sum(c, sum(d, e)));
// }

// int fac(int i) {
//     if (i == 0) {
//         return 1;
//     }
//     return fac(i-1) * i;
// }

int fib(int a) {
    if (a == 0 || a == 1) {
      return 1;
    }

    return fib(a-1) + fib(a-2);
}

// int a = 5;
// int b = 6;

int main() {
    // int c = 3234;
    // int a = 2;
    //
    // // a = 2;
    // // a + 1;
    // // a = a + 6;
    //
    // int b = 6;
    //
    // // char c = 'a';
    //
    // // a = a + b;
    //
    // b = sum(a, b); // b = 8
    //
    // summ(1, a, b, 4);
    //
    // fac(30);
    return fib(15);

    // while (b < a) {
    //   if (c != '6') {
    //     a = a - 1;
    //   }
    //   else {
    //     b = b+1;
    //   }
    // }

    // if (1 != 1) {
    //     10;
    // } else {
    //     20;
    // }

    // if (2 == 2 ) {
    //     30;
    // }

    // int a = 5;
    // while (a != 3) {
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
}
