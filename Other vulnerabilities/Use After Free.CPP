#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *)malloc(sizeof(int));
    *ptr = 10;
    free(ptr);
    printf("Use after free: %d\n", *ptr); // Undefined behavior
    return 0;
}
