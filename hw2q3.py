def main():
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

    :return:
    :rtype:
    """
    sentence = sentence.rstrip('!')
    encoded_sentence_list = []
    for char in sentence:
        new_char = get_new_char(char, shift)
        encoded_sentence_list.append(new_char)
    encoded_sentence = ''.join(encoded_sentence_list)
    return encoded_sentence


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
    new_letter_index = letter_difference + (shift_sign * (shift % 26))
    if new_letter_index >= 26:
        new_letter_index %= 26
    new_letter = letters[new_letter_index]
    if shift_sign == -1:
        new_letter = new_letter.upper()

    return new_letter


if __name__ == '__main__':
    main()
