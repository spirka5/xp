INVALID = -9999

def are_letters_valid(roman_letters):
    unique_letters = set()
    for letter in roman_letters:
        if not 'A' <= letter <= 'Z':
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

    for index in range(len(romanNumber)-1, -1, -1):
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



def tests():
    assert romanToInteger('A', 'A') == 1
    assert romanToInteger('A', 'AAA') == 3
    assert romanToInteger('A', 'AAAA') == -9999
    assert romanToInteger('AA', 'AA') == -9999
    assert romanToInteger('A', 'AXA') == -9999
    assert romanToInteger('123', '12') == -9999

    assert romanToInteger("IV", "VIII") == 8
    assert romanToInteger("A", "AAA") == 3
    assert romanToInteger("I", "IV") == -9999
    assert romanToInteger("IVXL", "LXXXIX") == 89
    assert romanToInteger("IAVXLCQDM", "QVA") == 1015
    assert romanToInteger("IVXLCDMPQRS", "SSS") == 300000
    assert romanToInteger("", "IV") == -9999
    assert romanToInteger("IVXLX", "IV") == -9999
    assert romanToInteger("IV", "") == -9999
    assert romanToInteger("12345", "12") == -9999


    assert romanToInteger('IVXLCDM', 'I') == 1
    assert romanToInteger('IVXLCDM', 'V') == 5
    assert romanToInteger('IVXLCDM', 'X') == 10
    assert romanToInteger('IVXLCDM', 'L') == 50
    assert romanToInteger('IVXLCDM', 'C') == 100
    assert romanToInteger('IVXLCDM', 'D') == 500
    assert romanToInteger('IVXLCDM', 'M') == 1000
    assert romanToInteger('IVXLCDM', 'IV') == 4
    assert romanToInteger('IVXLCDM', 'IX') == 9
    assert romanToInteger('IVXLCDM', 'XL') == 40
    assert romanToInteger('IVXLCDM', 'XC') == 90
    assert romanToInteger('IVXLCDM', 'CD') == 400
    assert romanToInteger('IVXLCDM', 'CM') == 900
    assert romanToInteger('IVXLCDM', 'MMXIV') == 2014
    assert romanToInteger('IVXLCDM', 'MMXCIX') == 2099
    assert romanToInteger('IVXLCDM', 'MMIM') == -9999     #2999  #wrong test
    assert romanToInteger('IVXLCDM', 'MMCMXCIX') == 2999  #correct test



    assert romanToInteger('IVXLCDM', 'MXMIV') == -9999  #1994 # wrong test
    assert romanToInteger('IVXLCDM', 'MCMXCIV') == 1994 # correct test
    assert romanToInteger('IVXLCDM', 'A') == -9999
    assert romanToInteger('IVXLCDM', 'IIII') == -9999
    assert romanToInteger('IVXLCDM', 'VXXV') == -9999
    assert romanToInteger('IVXLCDM', 'IVI') == -9999

    assert romanToInteger('IVXLCDM', 'MCMXCIV') == 1994
    assert romanToInteger('IVXLCDM', 'MMMCMXCIX') == 3999
    assert romanToInteger('IVXLCDM', 'CDXLIV') == 444
    assert romanToInteger('IVXLCDM', 'XC') == 90
    assert romanToInteger('IVXLCDM', 'DCCCXC') == 890
    assert romanToInteger('IVXLCDM', 'IIII') == -9999
    assert romanToInteger('IVXLCDM', 'VV') == -9999
    assert romanToInteger('IVXLCDM', 'IC') == -9999
    assert romanToInteger('IVXLCDM', 'IL') == -9999
    assert romanToInteger('IVXLCDM', 'VX') == -9999
    assert romanToInteger('IVXLCDM', 'MCMC') == -9999
    assert romanToInteger('IVXLCDM', 'IIV') == -9999
    assert romanToInteger('IVXLCDM', 'LC') == -9999
    assert romanToInteger('IVXLCDM', 'MMMM') == -9999
    assert romanToInteger('IVXLCDM', 'ABC') == -9999

if __name__ == '__main__':
    tests()