//Find the difference between 1^2 + 2^2 + ... + 100^2 and (1+2+...+100)^2

#include <stdio.h>

int main() {
	int sum1 = 0;
	int sum2 = 0;
	int i;
	for (i = 1; i <= 100; i++) {
		sum1 += i*i;
		sum2 += i;
	}
	sum2 = sum2*sum2;
	printf("%d\n", sum1 - sum2);
}