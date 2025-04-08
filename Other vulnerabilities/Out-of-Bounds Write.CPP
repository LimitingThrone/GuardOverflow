#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];
    strcpy(buffer, "This string is too long!"); // Overwrites memory beyond buffer size
    printf("%s\n", buffer);
    return 0;
}
