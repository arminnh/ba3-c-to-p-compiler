int f1(int q[][3]) {
	return 0;
}

int f2(int (*q[][3])[5]) {
	return 0;
}

int f3(int (*(**q[])[])[][2]) {
	return 0;
}

// TODO:  error: array type has incomplete element type
// int f4(int (*(**q[])[])[][]) {
// 	return 0;
// }

int main(void) {
	int (*q)[5][2];
    f1(q);
    f2(q);
	f3(q);

    int (**r[1])[];
    f1(r);
    f2(r);
    f3(r);

    int *(**s[2])[];
    f1(s);
    f2(s);
    f3(s);

    int (*(**t[5])[])[][2];
    f1(t);
	f2(t);
    f3(t);

    // TODO: error: type of formal parameter 1 is incomplete
    // int (*(**t2[])[])[][];
    // f3(t2);
}
