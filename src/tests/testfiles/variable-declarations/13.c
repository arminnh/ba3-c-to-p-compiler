int main(void) {
    float a = {5.0, 1, 2.0, '3', "aaa"};
    // ok, warning: excess elements in scalar initializer [enabled by default]
    return a;
}
