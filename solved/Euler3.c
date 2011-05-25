#include <stdio.h>

int main() {
	__int64 num = 851475143;
	int i = 2;
	int max = 0;
	while (i <= num) {
		if (num % i == 0) {
			printf("%d ", i);
			max = i;
			num = num/i;
			while (num % i == 0) {
				num = num/i;
			}
		}
		i++;
	}
	printf("%d\n", max);
}