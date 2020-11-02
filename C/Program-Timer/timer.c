#include<time.h>
#include<stdio.h>

// Placeholer function to edit:
void function(int a, int b){
    printf("%d + %d = %d\n", a, b, a+b);
}

int main(int argc, char *argv[])
{
    /*
    Create start and end clock variables of type `clock_t`
    and time the function.
    */
    clock_t start = clock();
    function(23, 54);
    clock_t end = clock();

    // Divide clock difference with CLOCKS_PER_SEC to convert time to seconds
    // and then typecast it to double.
    double time_taken = ((double)(end - start))/CLOCKS_PER_SEC;

    printf("function took %f seconds to execute\n", time_taken);

    return 0;
}
