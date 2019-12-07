def main():
    sentence = get_sentence()
    shift = get_shift()
    encoded_sentence = get_encoded_sentence(sentence, shift)


def get_sentence():
    print("Please enter a sentence to encrypt:")
    sentence = input()
    return sentence.lower()


def get_shift():
    print("Please enter the size of the shift:")
    shift = int(input())
    return shift


def get_encoded_sentence(sentence, shift):
    pass


def get_new_char(char, shift):
    new_char = char
    if char == '#':
        new_char = '*'
    elif char == '?':
        new_char = ''
    elif char.isalpha():
        new_char = get_new_letter(char, shift)
    return new_char


def get_new_letter(letter, shift):
    letters = [chr(ascii_value) for ascii_value in range(ord('a'), ord('z') + 1)]
    letter_difference = ord(letter) - ord('a')
    shift_sign = 1  # Assume that the letter is in even place
    if (letter_difference + 1) % 2 == 1:  # Check if the letter is in odd place
        shift_sign = -1
    new_letter = letters[letter_difference + (shift_sign * (shift % 26))]
    if shift_sign == -1:
        new_letter = new_letter.upper()

    return new_letter


if __name__ == '__main__':
    main()
