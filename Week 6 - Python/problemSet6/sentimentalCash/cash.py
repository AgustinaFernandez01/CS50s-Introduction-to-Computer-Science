def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    pennies = cents

    coins = quarters + dimes + nickels + pennies

    print(coins)


def get_cents():
    while True:
        try:
            cents = float(input("Change owed (in dollars): "))
            if cents >= 0:
                return round(cents * 100)
        except ValueError:
            pass


def calculate_quarters(cents):
    return cents // 25


def calculate_dimes(cents):
    return cents // 10


def calculate_nickels(cents):
    return cents // 5


if __name__ == "__main__":
    main()
