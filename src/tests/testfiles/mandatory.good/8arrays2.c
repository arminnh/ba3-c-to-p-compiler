int f(int a[3]) {
    return a[0]+a[1]+a[2];
}

int main()
{
    int a[3] = {1,2,3};
    a[2] = a[a[1]-1];
    a[1] = f(a);
    
    return 0;
}

