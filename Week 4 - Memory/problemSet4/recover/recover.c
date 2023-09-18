#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s IMAGE\n", argv[0]);
        return 1;
    }

    // Open the forensic image file
    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        fprintf(stderr, "Could not open %s\n", argv[1]);
        return 1;
    }

    // Initialize variables for reading
    BYTE buffer[BLOCK_SIZE];
    FILE *output_file = NULL;
    int jpeg_count = 0;

    // Iterate over blocks of data in the forensic image
    while (fread(buffer, 1, BLOCK_SIZE, input_file) == BLOCK_SIZE)
    {
        // Check for JPEG header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous output file (if open)
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            // Create new output file
            char filename[8];
            sprintf(filename, "%03i.jpg", jpeg_count++);
            output_file = fopen(filename, "w");
        }

        // Write data to output file (if open)
        if (output_file != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, output_file);
        }
    }

    // Close any remaining output file
    if (output_file != NULL)
    {
        fclose(output_file);
    }

    // Close input file
    fclose(input_file);

    return 0;
}
