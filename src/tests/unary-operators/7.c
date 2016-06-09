int main(void) {
    float f;
    float* ff = &f;
    f = *ff;
    f = ff;
}
