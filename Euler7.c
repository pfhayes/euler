//Find the 10001st prime.

#include <stdio.h>

int main () {
	int size = 1;
	int primes[10001];
	primes[0] = 2;
	int i;
	int curr = 3;
	for (i = 1; i < 10001; i++) {
		while (1) {
			int j;
			for (j = 0; j < size; j++) {
				if (curr % primes[j] == 0) {
					break;
				}
			}
			if (j==size) {
				primes [size] = curr;
				size++;
			}
			curr+=2;
			if (primes[size-1] == curr-2) {
				break;
			}
		}
	}
	printf("\n%d\n", primes[10000]);
}