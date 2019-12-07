def main():
    sentence = get_sentence()
    shift = get_shift()


def get_sentence():
    print("Please enter a sentence to encrypt:")
    sentence = input()
    return sentence.lower()


def get_shift():
    print("Please enter the size of the shift:")
    shift = int(input())
    return shift


def get_new_char(char, shift):
    new_char = char
    if char == '#':
        new_char = '*'
    elif char == '?':
        new_char = ''
    elif char.isalpha():
        new_char = get_new_letter(char, shift)


def get_new_letter(letter, shift):
    letters = [chr(ascii_value) for ascii_value in range(ord('a'), ord('z') + 1)]


if __name__ == '__main__':
    main()
