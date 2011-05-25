//Find the largest product of 5 consecutive digits in a 100-digit number

#include <stdio.h>

int main () {
	FILE *fp = fopen("./Euler8num.txt", "r");
	int k = 0;
	int max=0;
	char c1=0,c2=getc(fp),c3=getc(fp),c4=getc(fp),c5=getc(fp);
	for (k=0; k < 995; k++) {
		c1=c2;
		c2=c3;
		c3=c4;
		c4=c5;
		c5=getc(fp);
		int prod = (c1-48)*(c2-48)*(c3-48)*(c4-48)*(c5-48);
		printf("%d\n", prod);
		if (prod > max) {
			max = prod;
		}
	}
	fclose(fp);
	printf("%d\n",max);
}