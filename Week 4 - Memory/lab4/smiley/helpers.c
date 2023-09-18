#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Define the new color you want to use for non-black pixels
    RGBTRIPLE newColor;
    newColor.rgbtBlue = 255; // Change this to the desired blue value (0-255)
    newColor.rgbtGreen = 0;  // Change this to the desired green value (0-255)
    newColor.rgbtRed = 0;    // Change this to the desired red value (0-255)

    // Loop through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Check if the pixel is black
            if (image[i][j].rgbtBlue == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtRed == 0)
            {
                // Change the color of black pixels to the new color
                image[i][j] = newColor;
            }
        }
    }
}
