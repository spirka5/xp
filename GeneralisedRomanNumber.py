import skuska as s


DEFAULT_LETTERS = "-OIVXLCDM"


class GeneralisedRomanNumber:
    def __init__(self, letters):
        if not self.are_letters_valid(letters):
            letters = DEFAULT_LETTERS

        self.minusSign = letters[0]
        self.zeroSign = letters[1]
        self.letters = letters[2:]

    def are_letters_valid(self, letters):
        if len(letters) < 3:
            return False

        for letter in letters:
            if not ("A" <= letter <= "Z" or letter == "-"):
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
        max_number = (
            s.get_value_of_char(self.letters, self.letters[len(self.letters) - 1]) * 4
            - 1
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
        self.letters = romanNumber

    # Metóda vráti číselnú hodnotu členskej premennej.
    # Pokiaľ hodnota ešte nebola nastavená, vráti 0.
    def getValue(self):
        return 0
