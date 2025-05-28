import skuska as s

DEFAULT_LETTERS = "-OIVXLCDM"


class GeneralisedRomanNumber:
    def __init__(self, letters=DEFAULT_LETTERS):
        if not self.are_letters_valid(letters):
            letters = DEFAULT_LETTERS

        self.minusSign = letters[0]
        self.zeroSign = letters[1]
        self.letters = letters[2:]
        self.arabNumber = 0
        self.romanNumber = ""

    def are_letters_valid(self, letters):
        if len(letters) < 3:
            return False

        if not ("A" <= letters[0] <= "Z" or letters[0] == "-"):
            return False

        for letter in letters[1:]:
            if not ("A" <= letter <= "Z"):
                return False

        if len(letters) != len(set(letters)):
            return False

        return True

    # Vráti zoznam rímskych písmen včítane mínus a nuly, napr. "-OIVXLCDM"
    def getRomanLetters(self):
        return self.minusSign + self.zeroSign + self.letters

    # Metóda vráti najväčšie číslo, ktoré sa dá z daných
    # písmen rímskej abecedy napísať. Napr. 3999
    def maximum(self):
        index = len(self.letters) - 1
        if index % 2 == 0:
            max_number = (
                s.get_value_of_char(self.letters, self.letters[len(self.letters) - 1])
                * 4
                - 1
            )
        else:
            max_number = (
                s.get_value_of_char(self.letters, self.letters[len(self.letters) - 2])
                * 4
                - 1
                + s.get_value_of_char(self.letters, self.letters[len(self.letters) - 1])
            )

        return max_number

    # Metóda vráti najmenšie číslo, ktoré sa dá z daných
    # písmen rímskej abecedy napísať. Napr. -3999
    def minimum(self):
        return -self.maximum()

    # Ak je romanNumber prázdny reťazec, metóda neurobí nič a vráti false.
    # Inak metóda skontroluje, či je romanNumber korektné rímske číslo
    # napísané zo zadaných rímskych písmen. Prvé písmeno môže byť aj mínus.
    # Nula smie byť iba jeden znak. Ak nie je, metóda vráti false.
    # Inak vloží číslo do členskej premennej triedy.
    # Napr. "O", "IV", "CCC", "-LXI", "-XI"
    def setRomanNumber(self, romanNumber):
        ogRomanNumber = romanNumber
        if not romanNumber:
            return False

        value = 1
        if romanNumber[0] == self.minusSign:
            value = -1
            romanNumber = romanNumber[1:]

        if romanNumber[0] == self.zeroSign:
            if len(romanNumber) == 1:
                return 0
            else:
                return False

        intFromRoman = s.romanToInteger(self.letters, romanNumber)

        if intFromRoman == -9999:
            return False

        self.arabNumber = value * intFromRoman
        self.romanNumber = ogRomanNumber

    # Metóda vráti číselnú hodnotu členskej premennej.
    # Pokiaľ hodnota ešte nebola nastavená, vráti 0.
    def getValue(self):
        return self.arabNumber

    # Metóda vloží vstupné číslo do členskej premennej triedy, ak je číslo z povoleného intervalu <min, max> a vráti true. Inak iba vráti false.
    def setValue(self, value):
        if self.minimum() < value < self.maximum():
            self.arabNumber = value
            return True
        return False

    # Metóda vráti hodnotu členskej premennej ako rímske číslo.
    def getRomanNumber(self):
        return self.romanNumber


roman = GeneralisedRomanNumber("-O")
print(roman.getRomanLetters())
print(roman.letters)
print(roman.minimum())
roman.int_to_roman(8000)
