#include <stdio.h>

int main() {
    int arr[3] = {1, 2, 3};
    printf("Out-of-bounds read: %d\n", arr[5]); // Reading beyond allocated memory
    return 0;
}
