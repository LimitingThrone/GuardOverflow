#include <stdio.h>

int main() {
    int *ptr = NULL;
    printf("Dereferencing NULL: %d\n", *ptr); // Crash
    return 0;
}
