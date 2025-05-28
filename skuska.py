INVALID = -9999


def are_letters_valid(roman_letters):
    unique_letters = set()
    for letter in roman_letters:
        if not "A" <= letter <= "Z":
            return False
        unique_letters.add(letter)
    if len(unique_letters) != len(roman_letters):
        return False
    return True


def is_number_valid(roman_number):
    if type(roman_number) == int:
        return False
    if not roman_number:
        return False
    return True


def get_value_of_char(roman_letters, char):
    index = roman_letters.index(char)
    value = 10 ** (index // 2)
    if index % 2 == 1:
        value *= 5
    return value


def is_char_valid(roman_letters, char, prev_char, char_count):
    if char not in roman_letters:
        return False, INVALID

    if char != prev_char:
        char_count = 0
    char_count += 1

    if char_count > 3:
        return False, INVALID
    return True, char_count


def romanToInteger(romanLetters, romanNumber):
    if not are_letters_valid(romanLetters):
        return INVALID

    if not is_number_valid(romanNumber):
        return INVALID

    num = 0
    max = 0
    prev_char = None
    prev_prev_char = None
    char_count = 0

    for index in range(len(romanNumber) - 1, -1, -1):
        char = romanNumber[index]

        is_valid, char_count = is_char_valid(romanLetters, char, prev_char, char_count)
        if not is_valid:
            return INVALID

        value = get_value_of_char(romanLetters, char)
        if value >= max:
            if value % 10 == 5 and char == prev_char:
                return INVALID

            max = value
            num += max
        else:
            prev_char_value = get_value_of_char(romanLetters, prev_char)
            if value * 5 > prev_char_value or prev_char_value > value * 10:
                return INVALID
            if char == prev_prev_char:
                return INVALID

            num -= value

        prev_prev_char = prev_char
        prev_char = char
    return num
