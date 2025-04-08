#include <stdio.h>
#include <limits.h>

int main() {
    int max = INT_MAX;
    int result = max + 1; // Integer overflow
    printf("Integer Overflow: %d\n", result);
    return 0;
}
