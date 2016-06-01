char a() { return 'a'; }

int i() { return 2; }

int main() {
    int i[i()] = {1, 2, 3};
    char a[i()] = {a(), 'b', 'c'}

    return 0;
}
