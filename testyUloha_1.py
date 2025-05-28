import unittest
from GeneralisedRomanNumber import GeneralisedRomanNumber


# 1.uloha
class Test1(unittest.TestCase):
    # Roman letters
    def test_Alphabet_I(self):
        roman = GeneralisedRomanNumber("-OI")
        self.assertEqual(roman.getRomanLetters(), "-OI")

    def test_Alphabet_IVXLCDMQF(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMQF")
        self.assertEqual(roman.getRomanLetters(), "-OIVXLCDMQF")

    def test_DoubleLetter(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMSAC")
        self.assertEqual(roman.getRomanLetters(), "-OIVXLCDM")

    def test_WrongLetter(self):
        roman = GeneralisedRomanNumber("oivx")
        self.assertEqual(roman.getRomanLetters(), "-OIVXLCDM")

    # Maximum
    def test_OI(self):
        roman = GeneralisedRomanNumber("-OI")
        self.assertEqual(roman.maximum(), 3)
        self.assertEqual(roman.minimum(), -3)

    def test_O(self):
        roman = GeneralisedRomanNumber("-O")
        self.assertEqual(roman.minimum(), -3999)

    def test_max_V(self):
        roman = GeneralisedRomanNumber("-OB")
        self.assertEqual(roman.maximum(), 3)

    def test_max_IV(self):
        roman = GeneralisedRomanNumber("-OBC")
        self.assertEqual(roman.maximum(), 8)

    def test_max_IVXL(self):
        roman = GeneralisedRomanNumber("-OIVXL")
        self.assertEqual(roman.maximum(), 89)

    def test_IVXLCDM_1(self):
        roman = GeneralisedRomanNumber()
        self.assertEqual(roman.maximum(), 3999)

    def test_OIVXLCI(self):
        roman = GeneralisedRomanNumber("-OIVXLCI")
        self.assertEqual(roman.maximum(), 3999)

    def test_Empty(self):
        roman = GeneralisedRomanNumber("-O")
        self.assertEqual(roman.maximum(), 3999)

    def test_ABCDEFGHIJKLMN(self):
        roman = GeneralisedRomanNumber("-ABCDEFGHIJKLMN")
        self.assertEqual(roman.maximum(), 3999999)

    def test_NoSet(self):
        roman = GeneralisedRomanNumber("-OIVXL")
        self.assertEqual(roman.getValue(), 0)

    def test_I(self):
        roman = GeneralisedRomanNumber("-OI")
        roman.setRomanNumber("I")
        self.assertEqual(roman.getValue(), 1)

    def test_minusIII(self):
        roman = GeneralisedRomanNumber("-OI")
        roman.setRomanNumber("-III")
        self.assertEqual(roman.getValue(), -3)

    def test_IIII(self):
        roman = GeneralisedRomanNumber("-OI")
        roman.setRomanNumber("IIII")
        self.assertEqual(roman.getValue(), 0)

    def test_emptyAlphabet(self):
        roman = GeneralisedRomanNumber("")
        roman.setRomanNumber("MMDCIX")
        self.assertEqual(roman.getValue(), 2609)

    def test_ASDFG(self):
        roman = GeneralisedRomanNumber("-ZASDFG")
        roman.setRomanNumber("GGGSA")
        roman.setRomanNumber("-O")
        self.assertEqual(roman.getValue(), 306)

    def test_LLA(self):
        roman = GeneralisedRomanNumber("-OALP")
        roman.setRomanNumber("LA")
        roman.setRomanNumber("LLA")
        self.assertEqual(roman.getValue(), 6)

    def test_SQQQVII(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRS")
        roman.setRomanNumber("-II")
        roman.setRomanNumber("SQQQVII")
        self.assertEqual(roman.getValue(), 130007)

    def test_KLO(self):
        roman = GeneralisedRomanNumber("QPOILK")
        roman.setRomanNumber("PI")
        roman.setRomanNumber("KLO")
        self.assertEqual(roman.getValue(), 61)

    def test_IVXLCDMPQRSTUWY(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        roman.setRomanNumber("YWUSSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 16353046)

    # Wrong roman number
    def test_WrongNumber(self):
        roman = GeneralisedRomanNumber("-OIVXLCDM")
        roman.setRomanNumber("MMDXXL")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_IVI(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("IVI")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_IVV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("IVV")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_VV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("VV")
        self.assertEqual(roman.getValue(), 0)

    def test_VX(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("VX")
        self.assertEqual(roman.getValue(), 0)

    def test_IXV(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZEFGH")
        roman.setRomanNumber("IXV")
        self.assertEqual(roman.getValue(), 0)

    def test_CMMMXCIX(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("CMMMXCIX")
        self.assertEqual(roman.getValue(), 0)

    def test_MIVIVIII(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("MIVIVIII")
        self.assertEqual(roman.getValue(), 0)

    def test_RR(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRS")
        roman.setRomanNumber("RR")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_VIV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("VIV")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_IV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("IV")
        self.assertEqual(roman.getValue(), 4)

    def test_MIVIV(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("MIVIV")
        self.assertEqual(roman.getValue(), 0)

    def test_IIV(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("IIV")
        self.assertEqual(roman.getValue(), 0)

    def test_MMDXXL(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("IV")
        roman.setRomanNumber("MMDXXL")
        self.assertEqual(roman.getValue(), 4)

    def test_IVX_VX(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("VX")
        self.assertEqual(roman.getValue(), 0)

    def test_IVX_IXV(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("IXV")
        self.assertEqual(roman.getValue(), 0)

    def test_IIX(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("IIX")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest1(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("MMMM")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest2(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("CDCD")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest3(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("CDC")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest4(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("IXV")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest5(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("VX")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest6(self):
        roman = GeneralisedRomanNumber("-OIVXL")
        roman.setRomanNumber("XLIX")
        self.assertEqual(roman.getValue(), 49)

    def test_newTest7(self):
        roman = GeneralisedRomanNumber("-OABC")
        roman.setRomanNumber("BB")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest8(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRS")
        roman.setRomanNumber("RR")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest9(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRS")
        roman.setRomanNumber("XVIX")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest10(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZ")
        roman.setRomanNumber("ZUUUTSSSRQMPCCCXIV")
        self.assertEqual(roman.getValue(), 53864314)

    def test_newTest11(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZ")
        roman.setRomanNumber("MMDCCCLXXXVIII")
        self.assertEqual(roman.getValue(), 2888)

    def test_newTest12(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZ")
        roman.setRomanNumber("DCCLXXXIX")
        self.assertEqual(roman.getValue(), 789)

    def test_newTest13(self):
        roman = GeneralisedRomanNumber("-OIVXLX")
        roman.setRomanNumber("MMI")
        self.assertEqual(roman.getValue(), 2001)

    def test_newTest14(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("XXXIXX")
        self.assertEqual(roman.getValue(), 0)

    def test_newTest15(self):
        roman = GeneralisedRomanNumber("-OIVXLX")
        roman.setRomanNumber("MMI")
        self.assertEqual(roman.getValue(), 2001)

    def test_newTest16(self):
        roman = GeneralisedRomanNumber("-OIVXLX")
        roman.setRomanNumber("MMI")
        self.assertEqual(roman.getValue(), 2001)

    def test_newTest17(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("CMCD")
        self.assertEqual(roman.getValue(), 0)

    def test_TestEfektivnosti(self):
        for _ in range(1000):
            roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
            roman.setRomanNumber("YWUSSSRMMMXLVII")
            self.assertEqual(roman.getRomanNumber(), "YWUSSSRMMMXLVII")


if __name__ == "__main__":
    unittest.main()
