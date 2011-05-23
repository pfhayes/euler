//Find the sums of all the primes below 2000000

#include <stdio.h>
#include <string.h>

int main (int argc, char *argv[]) {
	int num = atoi(argv[1]);
	int size = 1;
	double sum = 2;
	int primes[2000000];
	primes[0] = 2;
	int i;
	int curr = 1;
	while (curr+2 < num) {
		curr+=2;
		int j;
		for (j = 0; j < size; j++) {
			if (curr % primes[j] == 0) {
				break;
			}
		}
		if (j==size) {
			primes [size] = curr;
			sum += curr;
			size++;
		}
	}
	printf("%f\n", sum);
	i=0;
	sum=0;
	while (primes[i] < num && primes[i] > 0) {
		sum+= primes[i];
		i++;
	}
	printf("%f\n", sum);
}