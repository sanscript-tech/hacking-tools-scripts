#include<time.h>
#include<stdio.h>

void function(int a, int b){
    printf("%d + %d = %d\n", a, b, a+b);
}

int main(int argc, char *argv[])
{
    clock_t start = clock();
    function(23, 54);
    clock_t end = clock();

    double time_taken = ((double)(end - start))/CLOCKS_PER_SEC;

    printf("function took %f seconds to execute\n", time_taken);

    return 0;
}
