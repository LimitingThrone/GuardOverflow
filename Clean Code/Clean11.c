#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int size, i, sum = 0;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    arr = (int *)malloc(size * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Exit with an error code
    }

    printf("Enter %d elements:\n", size);
    for (i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    printf("You entered: ");
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nSum of the elements: %d\n", sum);

    free(arr);

    return 0;
}
