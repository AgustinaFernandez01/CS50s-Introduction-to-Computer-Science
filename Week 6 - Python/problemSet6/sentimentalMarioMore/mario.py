def main():
    height = 0
    while True:
        height_input = input("Height: ")
        if height_input.isdigit():
            height = int(height_input)
            if 1 <= height <= 8:
                break

    for line in range(height):
        spaces = height - line - 1
        hashes = line + 1

        # Print spaces
        print(" " * spaces, end="")

        # Print left hashes
        print("#" * hashes, end="  ")

        # Print right hashes
        print("#" * hashes)


if __name__ == "__main__":
    main()
