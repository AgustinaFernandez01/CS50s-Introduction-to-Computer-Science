from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    words = text.split()
    return len(words)


def count_sentences(text):
    sentences = text.count(".") + text.count("!") + text.count("?")
    return sentences


if __name__ == "__main__":
    main()
