def main():
    """
    The program gets from the user a sentence and a non negative number, and encrypts the sentence,
    according to the following rules:
        - Every number sign (#) turns into asterisk (*).
        - Every exclamation mark (!) in the end of the sentence is removed.
        - Every question mark (?) is removed.
        - Every letter gets shifted backwards or forward in a cyclic shift,
          according to the shift number the parity of the letter.

    """
    sentence = get_sentence()
    shift = get_shift()
    encoded_sentence = get_encoded_sentence(sentence, shift)
    print(encoded_sentence)


def get_sentence():
    """
    Gets a sentence from the user, converts all of the letters to lowercase form,
    and returns the sentence.

    :return: The lowercase sentence
    :rtype: str
    """
    print("Please enter a sentence to encrypt:")
    sentence = input()
    sentence = sentence.lower()
    return sentence


def get_shift():
    """
    Gets the shift number from the user, and returns it.

    :return: The shift number
    :rtype: int
    """
    print("Please enter the size of the shift:")
    shift = int(input())
    return shift


def get_encoded_sentence(sentence, shift):
    """
    Generates the encoded sentence, and returns it.

    :param sentence: The sentence to encode
    :type sentence: str
    :param shift: The shift number
    :type shift: int

    :return: The encoded sentence
    :rtype: str
    """
    sentence = sentence.rstrip('!')
    encoded_sentence_list = []  # List of the letters of the encoded sentence
    for char in sentence:
        new_char = get_new_char(char, shift)
        encoded_sentence_list.append(new_char)
    encoded_sentence = ''.join(encoded_sentence_list)
    return encoded_sentence


def get_new_char(char, shift):
    """
    Gets the new char that replaces the current one in the encoded sentence.

    :param char: The char
    :type char: str
    :param shift: The shift number
    :type shift: int

    :return: The new char
    :rtype: str
    """
    new_char = char  # Assume that the char doesn't need to be changed
    if char == '#':
        new_char = '*'
    elif char == '?':
        new_char = ''
    elif char.isalpha():  # The char is a letter
        new_char = get_new_letter(char, shift)
    return new_char


def get_new_letter(letter, shift):
    """
    Gets the new letter by cyclic shift of the current letter, according to the shift parameter.

    :param letter: The letter
    :type letter: str
    :param shift: The shift number
    :type shift: int

    :return: The new letter
    :rtype: str
    """
    letters = [chr(ascii_value) for ascii_value in range(ord('a'), ord('z') + 1)]  # List of all lowercase letters
    letter_difference = ord(letter) - ord('a')
    shift_sign = 1  # Assume that the letter is in even place
    if (letter_difference + 1) % 2 == 1:  # Check if the letter is in odd place
        shift_sign = -1
    new_letter_index = letter_difference + (shift_sign * (shift % 26))
    if new_letter_index >= len(letters):
        new_letter_index %= len(letters)
    new_letter = letters[new_letter_index]
    if shift_sign == -1:  # The letter is in odd place
        new_letter = new_letter.upper()

    return new_letter


if __name__ == '__main__':
    main()
