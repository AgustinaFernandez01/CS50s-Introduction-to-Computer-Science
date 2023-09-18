#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size

    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // Calculate number of years
    int years = 0;
    int current_size = start_size;
    while (current_size < end_size)
    {
        int births = current_size / 3;
        int deaths = current_size / 4;
        current_size = current_size + births - deaths;
        years++;
    }

    // Print number of years
    printf("Years: %d\n", years);
}
