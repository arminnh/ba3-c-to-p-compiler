#include <stdio.h>

void areaperi ( int r, float *a, float *p ) {
    *a = 3.14 * (float) r * (float) r;
    *p = (float) 2 * 3.14 * (float) r;
}

int main( ) {
    int radius;
    float area, perimeter;
    printf("\nEnter radius of a circle: ");
    scanf("%d", &radius);

    areaperi(radius, &area, &perimeter);

    printf("Area = %f", area);
    printf("\nPerimeter = %f", perimeter);
}
