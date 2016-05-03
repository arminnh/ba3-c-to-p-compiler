int aa = 10;
int bb = 11;

int main(void)
{
    //int a[10] = {function()};
    int e = {1, 6};

    {
        float b = 1.0;
        float c = 7.0, d = 8.0;
        char f = 'a', *ff = "aaa"; // fix
        float * const aeiojef = {1.0, 2.0, 3.0};

        {
            const int g[] = {1, 2, 3};
            int const h = 5;

            {
                int i[7] = {1, 2};
            }
        }

        int const j[1+8+9] = {1, 2, 3};
        int k[5], l[] = {1, 2}, m[1] = {6};
        // int o = 2, q[] = {1}, r[5] = {1, 2*e, 3, 4*a+4, 5}, s[5*a];
    }

    int t = aa, u = bb;

	const int aghf, *bfh, * const ccbv;
	int const ahga, *dfab, * const afc;
	int const * const * abab, *atab, * const caa;

    char hello[] = "5", ccc = 'c', *str = "string";
    *hello = 'u';

    int *arrint[] = {&e};

    {
    	char helloo[] = {'5'};
    	char hello[6+5*8] = "hello", ccc = 'c', *str = "string", aaaa[] = "hier hebben we aan gedacht";

    	int i = 5;
    	int *arrint[1] = {&i};

    	char* h = hello;
    	h++;

    	*hello = 'u';

    	int const bb = 1;
    	int bbb = 2;
    	int const constarr[2] = {1, 2};

    	h = "newst";

    	int *aaa;
    	int aaaaa[] = {1, 2, 3};
    	aaa = aaaaa;

    	const int* p;
    }

    int asdfa[3];
    int asdfas[] = {1, 2, 3};
    int aasdfad[3] = {1, 2, 3};
    char aasdfasdf[5] = "abc";
    char *aassfdfasdf = "aaa";

	return 0;
}

int aaa = 1;
int bbb = 2;
