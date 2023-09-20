def main():
    # Get the credit card number from the user
    card_number = input("Number: ")

    if not card_number.isdigit() or int(card_number) <= 0:
        print("INVALID")
        return

    card_length = len(card_number)

    # Check the card's validity using Luhn's algorithm
    total = 0
    for i in range(card_length - 2, -1, -2):
        digit = int(card_number[i]) * 2
        if digit > 9:
            digit -= 9
        total += digit

    for i in range(card_length - 1, -1, -2):
        total += int(card_number[i])

    # Check the card type
    if total % 10 == 0:
        if card_length == 15 and card_number[:2] in ("34", "37"):
            print("AMEX")
        elif card_length == 16 and card_number[:2] in ("51", "52", "53", "54", "55"):
            print("MASTERCARD")
        elif (card_length == 13 or card_length == 16) and card_number[0] == "4":
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
