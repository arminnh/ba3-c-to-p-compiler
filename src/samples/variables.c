int aa = 10;
int bb = 11;

int main(void)
{
    int a;
    int e = 1;

    {
        float z = (float) z;
        float b = 1.0;
        float c = 2.7, d = 8.0;
        char f = 'a', *ff = "aaa";

        {
            const int g[] = {1, 2, 3};
            int const h = 5; // TODO for extras: dont't allow const variable declaration without initial value

            {
                int i[7] = {1, 2}; // {1, 2, 0, 0, 0, 0, 0}
            }
        }

        int const j[1+8+9] = {1, 2, 3};
        int k[5], l[] = {1, 2}, m[1] = {6};
        int o = 2, q[] = {1}, r[5] = {1, 2*e, 3, 4*a+4, 5}, s[5*a];
    }

    int t = aa, u = bb;
    // aaa and bbb are undeclared here

    char hello[] = "5", ccc = 'c', *str = "string";
    *hello = 'u';

    int *arrint[] = {&e};

    int *as;
    int *asd = as;

    // int asdf[]; // error: array size missing in 'asdf'
    int asdfa[3];
    int asdfas[] = {1, 2, 3};
    int aasdfad[3] = {1, 2, 3};
    char aasdfasdf[5] = "abc";
    char *aassfdfasdf = "aaa";

    return 1;
}

int aaa = 1;
int bbb = 2;
