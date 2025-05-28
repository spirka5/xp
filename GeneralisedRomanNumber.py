class GeneralisedRomanNumber:
    def __init__(self, letters):
        self.letters = letters

    # Vráti zoznam rímskych písmen včítane mínus a nuly, napr. "-OIVXLCDM"
    def getRomanLetters(self):
        return self.letters
    # Metóda vráti najväčšie číslo, ktoré sa dá z daných
    # písmen rímskej abecedy napísať. Napr. 3999
    def maximum(self):
        return 0
    # Metóda vráti najmenšie číslo, ktoré sa dá z daných
    # písmen rímskej abecedy napísať. Napr. -3999
    def minimum(self):
        return 0

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
