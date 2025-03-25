#include <stdio.h>

int main() {
    FILE *file;
    char buffer[256];
    size_t bytesRead;

    file = fopen("example.txt", "r");

    if (file == NULL) {
        printf("Error: Could not open file.\n");
        return 1;
    }

    printf("File contents:\n");
    while ((bytesRead = fread(buffer, 1, sizeof(buffer) - 1, file)) > 0) {
        buffer[bytesRead] = '\0'; // Null-terminate the buffer
        printf("%s", buffer);
    }

    fclose(file);

    return 0;
}
