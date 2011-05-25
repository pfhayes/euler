#include <stdio.h>

int main() {
	long int sum=0;
	int a = 1;
	int b = 2;
	while (b < 4000000) {
		sum += b;
		int newa = a + 2*b;
		b = 2*a + 3*b;
		a = newa;
		printf("%d ", b);
	}
	printf("%d\n", sum);
}