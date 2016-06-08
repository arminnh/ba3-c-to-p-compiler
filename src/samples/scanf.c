#include <stdio.h>

void areaperi ( int r, float *a, float *p ) {
    *a = 3.14 * (float) r * (float) r;
    *p = (float) 2 * 3.14 * (float) r;
}

void main( ) {
    const int radius;
    float area, perimeter;
    printf("nEnter radius of a circle ");
    scanf("%d", &radius);

    areaperi(radius, &area, &perimeter);

    printf("Area = %f", area);
    printf("nPerimeter = %f", perimeter);




    int length, breadth;

    printf("\nEnter the Length of Rectangle : ");
    scanf("%d", &length);

    printf("\nEnter the Breadth of Rectangle : ");
    scanf("%d", &breadth);





    int arr1[30], arr2[30], i, num;

    printf("\nEnter no of elements :");
    scanf("%d", &num);

    //Accepting values into Array
    printf("\nEnter the values :");
    for (i = 0; i < num; i++) {
        scanf("%d", &arr1[i]);
    }

    /* Copying data from array 'a' to array 'b */
    for (i = 0; i < num; i++) {
     arr2[i] = arr1[i];
    }

    //Printing of all elements of array
    printf("The copied array is :");
    for (i = 0; i < num; i++)
        printf("\narr2[%d] = %d", i, arr2[i]);
}
