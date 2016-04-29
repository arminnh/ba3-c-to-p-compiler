int main(void)
{
    float c[2] = {1.1, 2.2};
    (1 || 2.0 ? c[0] : 0);

    return 0;
}
