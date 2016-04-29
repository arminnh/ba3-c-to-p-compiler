int main(void) {
    int i = 0;
    !i;
    i = !(i && 5 || !3);
    &i;
    ++i;
    --i;
    i++;
    --i;
    int* ii = &i;
    i = *ii;
    
    float f = 7.8;
    float* ff = &f;
    f = *ff;
}
