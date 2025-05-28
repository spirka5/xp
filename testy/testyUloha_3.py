import unittest
from riesenie2025 import GeneralisedRomanNumber


# 3.uloha
class Test3(unittest.TestCase):
    def test_I_I_5(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setValue(5)
        self.assertEqual(roman.getValue(), 5)

    def test_Basic(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertTrue(romanNumber.calculator("I+I"))
        self.assertEqual(romanNumber.getRomanNumber(), "II")

    def test_AddZero(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertTrue(romanNumber.calculator("IV + O"))
        self.assertEqual(romanNumber.getRomanNumber(), "IV")

    def test_AddToZero(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertTrue(romanNumber.calculator("O + IV"))
        self.assertEqual(romanNumber.getRomanNumber(), "IV")

    def test_MinusMinus(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertTrue(romanNumber.calculator("I - -I"))
        self.assertEqual(romanNumber.getRomanNumber(), "II")

    def test_TwoMinus(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertTrue(romanNumber.calculator("-I + -I"))
        self.assertEqual(romanNumber.getRomanNumber(), "-II")

    def test_Sum(self):
        romanNumber = GeneralisedRomanNumber()
        romanNumber.calculator("L+XL")
        self.assertEqual(romanNumber.getRomanNumber(), "XC")

    def test_Subtraction(self):
        romanNumber = GeneralisedRomanNumber()
        romanNumber.calculator("MMDCCLXXXIII-MDCLXVI")
        self.assertEqual(romanNumber.getRomanNumber(), "MCXVII")

    def test_Division(self):
        romanNumber = GeneralisedRomanNumber()
        romanNumber.calculator("MMMDC/MD")
        self.assertEqual(romanNumber.getRomanNumber(), "II")

    def test_Multiplication(self):
        romanNumber = GeneralisedRomanNumber()
        romanNumber.calculator("XIV*VI")
        self.assertEqual(romanNumber.getRomanNumber(), "LXXXIV")

    def test_subtractSmaller(self):
        romanNumber = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        romanNumber.calculator("YYMMDCCLXXXIII - YYMDCLXVI")
        self.assertEqual(romanNumber.getRomanNumber(), "MCXVII")

    def test_subtractBigger(self):
        romanNumber = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        romanNumber.calculator("YYMDCLXVI - YYMMDCCLXXXIII")
        self.assertEqual(romanNumber.getRomanNumber(), "-MCXVII")

    def test_subtractEqual(self):
        romanNumber = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        romanNumber.calculator(" - YYMMDCCLXXXIII - - YYMMDCCLXXXIII ")
        self.assertEqual(romanNumber.getRomanNumber(), "O")

    # Wrong expressions
    def test_empty(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator(""))

    def test_twoOperators(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("MMDC-*MD"))

    def test_wrongNumber(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("I-MMMIM"))

    def test_missingOperator(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("MXII"))

    def test_missingSecond(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("MMDCCLXXXII+"))

    def test_missingFirst(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("-MMDCCLXXXII"))

    def test_moreLetters(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("MMDC-MD a"))

    def test_unknownOperator(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("X^II"))

    def test_wrongLetter(self):
        romanNumber = GeneralisedRomanNumber()
        self.assertFalse(romanNumber.calculator("GL+V"))

    def test_resultTooSmall(self):
        romanNumber = GeneralisedRomanNumber("-OIVX")
        self.assertFalse(romanNumber.calculator("-XXX - XXX"))

    def test_resultTooBig(self):
        romanNumber = GeneralisedRomanNumber("-OIVX")
        self.assertFalse(romanNumber.calculator("XXX + XX"))

    def test_TestEfektivnosti(self):
        romanNumber = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        for _ in range(1000):
            romanNumber.calculator("YYMMDCCLXXXIII-YYMDCLXVI")
        self.assertEqual(romanNumber.getRomanNumber(), "MCXVII")


if __name__ == '__main__':
    unittest.main()
