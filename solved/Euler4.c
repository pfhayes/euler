//Find the largest palindrome that is the product of two 3-digit numbers

#include <stdio.h>

int main () {
	int x = 999;
	for (; x > 100; x--) {
		int pali = x/100 * 100000 + (x%100) / 10 * 10000 + (x%10) * 1000 + (x%10) * 100 + (x%100) / 10 * 10 + x / 100;
		int i;
		for (i=999; i > 900; i--) {
			if (pali % i == 0) {
				printf("%d %d\n", pali, pali/i);
			}
		}
	}
}