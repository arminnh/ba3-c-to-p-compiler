int sub(const int a, int const * const b, const const const c);

// TODO this should give the same warning 'type defaults to int', but gives error "parameters don't match"
int sub(const int a, int const * const b, const const const c) {
    return 0;
}

int main() {
    return 0;
}
