#include <stdio.h>

int main() {
    FILE *file;
    char ch;

    file = fopen("example.txt", "r");

    if (file == NULL) {
        printf("Error: Could not open file.\n");
        return 1;
    }

    printf("File contents:\n");
    while ((ch = fgetc(file)) != EOF) {
        printf("%c", ch);
    }

    fclose(file);

    return 0;
}
