//Find the only pythagorean triplet (a,b,c) where a^2+b^2=c^2 such that a+b+c=1000

#include <stdio.h>

int main() {
	int a;
	int b;
	for (a=1; a < 1000; a++) {
		for (b=1; b < 1000; b++) {
			if ((a-1000)*(b-1000)==500000) {
				printf("%d %d\n", a, b);
			}
		}
	}
}