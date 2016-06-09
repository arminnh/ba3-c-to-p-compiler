int main(void) {
	int a = 5, b = 10;

	char *s = "hello";

	float t;

	&a;
	&b;
	&s;
	&t;

	int * aa    = &a;
	int * bb    = &b;
	char ** ss  = &s;
	char * sss  = &s;
	float * tt  = &t;

	return 0;
}
