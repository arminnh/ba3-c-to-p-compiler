int f1(int q[][3]) {
	return 0;
}

int f2(int (*q[][3])[5]) {
	return 0;
}

int f3(int (*(**q[])[])[][2]) {
	return 0;
}

int main(void) {
	int q[10][3];
	f1(q);
	f2(q);
    f3(q);

    int (*r[20][3])[5];
	f1(r);
	f2(r);
    f3(r);

    int (*(**s[30])[])[][2];
	f1(s);
	f2(s);
    f3(s);
}
