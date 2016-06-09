#include <stdio.h>

int main() {
	float celsius, fahrenheit;

	printf("\nEnter temp in Celsius : ");
	scanf("%f", &celsius);

	fahrenheit = (1.8 * celsius) + (float) 32;
	printf("\nTemperature in Fahrenheit : %f ", fahrenheit);

	return (0);
}
