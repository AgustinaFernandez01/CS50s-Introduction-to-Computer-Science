#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int line = 0; line < height; line++)
    {
        for (int space = height - line - 1; space > 0; space--)
        {
            printf(" ");
        }
        for (int hash = 0; hash < line + 1; hash++)
        {
            printf("#");
        }
        printf("  ");
        for (int right_hash = 0; right_hash < line + 1; right_hash++)
        {
            printf("#");
        }
        printf("\n");
    }
}