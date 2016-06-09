int main() {
    int a[2];
    int *b[2];
    int (*c)[2];

    int * d[2][3];
    int (* e[2])[3];
    int *(* f[2])[3];

    int *** g1[2][3][4];
    int *** ((((g2)[2])[3])[4]);
    int (*(*(* ((((g3)[2])[3])[4]))));
    int **(* h)[2][3][4];
    int *(** i[2][3])[4];
    int (*(*(* j)[2])[3])[4];

    char aa = a;
    char bb = b;
    char cc = c;
    char dd = d;
    char ee = e;
    char ff = f;
    char gg1 = g1;
    char gg2 = g2;
    char gg3 = g3;
    char hh = h;
    char ii = i;
    char jj = j;
}
