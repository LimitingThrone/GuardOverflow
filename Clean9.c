#include <stdio.h>
#include <ctype.h>

int main() {
    FILE *file;
    char ch;
    int lines = 0, words = 0, characters = 0, inWord = 0;

    file = fopen("example.txt", "r");

    if (file == NULL) {
        printf("Error: Could not open file.\n");
        return 1;
    }

    while ((ch = fgetc(file)) != EOF) {
        characters++;
        if (ch == '\n') {
            lines++;
        }
        if (isspace(ch)) {
            inWord = 0;
        } else if (!inWord) {
            inWord = 1;
            words++;
        }
    }

    fclose(file);

    printf("Lines: %d\nWords: %d\nCharacters: %d\n", lines, words, characters);

    return 0;
}
