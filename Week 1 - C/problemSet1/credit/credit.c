#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get the credit card number from the user
    long long card_number;
    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number <= 0);

    // Calculate checksum using Luhn's algorithm
    int sum = 0;
    int digit_count = 0;
    long long temp = card_number;

    while (temp > 0)
    {
        int last_digit = temp % 10;

        if (digit_count % 2 == 1)
        {
            int doubled_digit = last_digit * 2;
            sum += (doubled_digit % 10) + (doubled_digit / 10);
        }
        else
        {
            sum += last_digit;
        }

        temp /= 10;
        digit_count++;
    }

    // Check the card's validity and its type
    if (sum % 10 == 0)
    {
        int first_digit = card_number / 10 % 10;
        int second_digit = card_number / 100 % 10;

        if ((digit_count == 15) && (second_digit == 3) && ((first_digit == 4) || (first_digit == 7)))
        {
            printf("AMEX\n");
        }
        else if ((digit_count == 16) && (second_digit >= 1) && (second_digit <= 5))
        {
            printf("MASTERCARD\n");
        }
        else if ((digit_count == 13 || digit_count == 16) && (first_digit == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}