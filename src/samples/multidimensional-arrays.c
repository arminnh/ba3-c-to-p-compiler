#include <stdio.h>

int main() {
    // const int aa[2][3][4] = {
    //   {
    //     {10, 11, 10, 11}, {12, 13, 12, 13}, {12, 345, 568, 1}
    //   },
    //   {
    //     {14, 15, 14, 15}, {16, 17, 16, 17}, {41, 345, 74, 34}
    //   }
    // };

    // const int a[][2][2] = {
    //     {
    //         {10, 11}, {12, 13}
    //     },
    //     {
    //         {14, 15}, {16, 17}
    //     }
    // };
    //
    // const int arr[] = {10, 20, 30};
    //
    // printf("%i\n", *(**a + 1));
    // printf("%i\n", a[0][1][0]);
    // printf("%i\n", *(arr+1) + 1);


    int n = 5;
    int *nn = &n;
    int **nnn = &nn;
    int arr2[n];

    int * josse [10] = { nn, nn, nn, nn, nn, nn, nn, nn, nn, nn };

    // TODO: bij het alloceren van een array, allocceer vanaf de bovenkant van TypeInfo.indirections tot dat je een niet-array indirectie tegenkomt 
    int *(* a2[2])[10] = { &josse, &josse };
    a2[0] = &josse;

    // int ** a2[5][10] = {
    //     { 0, 1, 2, 2 },
    //     { 0, 1, 2 },
    //     { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
    //     { 0, 0, 0, 0, 0, 0, 7, 0, 0, 0 },
    //     { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }
    // };

    // int *a3 = a[2];

    // printf("%i, %i\n", a2[1][2], a2[3][6]);

    // int a4 = 1, b = 2, c[] = {1, 2}, d[][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, f[] = {};
    //
    // f[100] = 40;
    // printf("%i\n", f[100]/*[12]*/);
}


int sum(int const * const * * a);
int sub(const int * const * * a);

int previousMain() {
	//char hello[] = {'5'};
	char hello[6+5*8] = "hello", ccc = 'c', *str = "string", aaaa[] = "hier heb ik niet aan gedacht";

	int i = 5;
	int *arrint[1] = {&i};

	char* h = hello;
	h++;

	//int j = "hello"; // error

	*hello = 'u';
	// *hello = "uu"; // mag niet werken

	int const bb = 1;
	int bbb = 2;
	int const constarr[2] = {1, 2};
	// constarr[0] = bb; // TODO for extras: error: assignment of read-only location 'constarr[0]'


	// char* = char[]
	h = "newst";
	// h = 'n'; //error

	int *aaa;
	int aaaaa[] = {1, 2, 3};
	aaa = aaaaa;

	// printf("%s\n", hello);

	const int* p;
	// int* q = p; // TODO for extras: warning: initialization discards 'const' qualifier from pointer target type

	const int a, *b, * const c;
	int const aa, *ab, * const ac;
	int const * const * abab, *aab, * const caa;

	/*char *y[5][6];
	char (*y2)[5][4];
	char *(y3[5])[4];
	char ((((*((y4[5]))))[4]));*/

	char y5[5];
	char (y6)[5];
	char (y7[5]);
	char ((((((y8[5]))))));
	char (y9)[5];
	int (abla) = 5, blabla = 3, ((ablaba)[3]) = {1, 2, 3};

	char *y[5];
	char (*y2)[5];
	char *(y3[5]);
	char ((((*((y4[5]))))));
	char *(*y10[4]);

	int a123[] = {5, 6};
	int a234[2];
	a234 = a123;
	int *a345 = a123;
	a123 = a345;

	char *s123 = h;
	hello = s123;

	char hello2[46];
	hello2 = hello;


	printf("%s\n", "hello");
	printf("%s\n", hello);
	printf("%s\n", &hello);
    printf("%s\n", h);
}
