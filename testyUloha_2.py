import unittest
from GeneralisedRomanNumber import GeneralisedRomanNumber


# 2.uloha
class Test2(unittest.TestCase):
    def test_I_I_5(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setValue(5)
        self.assertEqual(roman.getValue(), 5)

    def test_IVXLCDMPQRSTUWYZ_53864324(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZ")
        roman.setValue(53864324)
        self.assertEqual(roman.getValue(), 53864324)

    def test_minus3296(self):
        roman = GeneralisedRomanNumber()
        roman.setValue(-3827)
        self.assertEqual(roman.getRomanNumber(), "-MMMDCCCXXVII")

    def test_Zero(self):
        roman = GeneralisedRomanNumber()
        self.assertTrue(roman.setValue(0))
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IVXLCDM_MAX_plus(self):
        roman = GeneralisedRomanNumber()
        self.assertFalse(roman.setValue(4000))
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IVX_39(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setValue(39)
        self.assertEqual(roman.getRomanNumber(), "XXXIX")

    # Get roman number
    def test_IVXLCDMPQRSTUWY_16353046(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        roman.setValue(16353046)
        self.assertEqual(roman.getRomanNumber(), "YWUSSSRMMMXLVI")

    def test_ABCD_minus80(self):
        roman = GeneralisedRomanNumber("-OABCD")
        roman.setValue(-80)
        self.assertEqual(roman.getRomanNumber(), "-DCCC")

    def test_IVXLCDMPQRSTUWYZ_53864323(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZ")
        roman.setValue(-53864323)
        self.assertEqual(roman.getRomanNumber(), "-ZUUUTSSSRQMPCCCXXIII")

    def test_OMPQRSTUWYZABCD(self):
        roman = GeneralisedRomanNumber("-OMPQRSTUWYZABCD")
        roman.setValue(7777777)
        self.assertEqual(roman.getRomanNumber(), "DCCBAAZYYWUUTSSRQQPMM")

    def test_O(self):
        roman = GeneralisedRomanNumber("-NMPQRSTUWYZABCD")
        roman.setValue(0)
        self.assertEqual(roman.getRomanNumber(), "N")

    def test_minusIII(self):
        roman = GeneralisedRomanNumber("-OI")
        roman.setValue(-3)
        self.assertEqual(roman.getValue(), -3)

    def test_emptyAlphabet(self):
        roman = GeneralisedRomanNumber("")
        roman.setValue(2609)
        self.assertEqual(roman.getValue(), 2609)

    def test_rewriteCorrect(self):
        roman = GeneralisedRomanNumber("-OALP")
        roman.setValue(7)
        self.assertTrue(roman.setValue(-39))
        self.assertEqual(roman.getValue(), -39)

    def test_rewriteTooBig(self):
        roman = GeneralisedRomanNumber("-OALP")
        roman.setValue(6)
        self.assertFalse(roman.setValue(40))
        self.assertEqual(roman.getValue(), 6)

    def test_rewriteTooSmall(self):
        roman = GeneralisedRomanNumber("-OALP")
        roman.setValue(-7)
        self.assertFalse(roman.setValue(-40))
        self.assertEqual(roman.getValue(), -7)

    def test_IVXLCDMPQRSTUWY(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        roman.setValue(16353046)
        self.assertEqual(roman.getValue(), 16353046)

    def test_NoSet(self):
        roman = GeneralisedRomanNumber("-OIVXL")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_minusIII_t(self):
        roman = GeneralisedRomanNumber("-OI")
        roman.setRomanNumber("-III")
        self.assertEqual(roman.getRomanNumber(), "-III")

    def test_emptyAlphabet_t(self):
        roman = GeneralisedRomanNumber("")
        roman.setRomanNumber("MMDCIX")
        self.assertEqual(roman.getRomanNumber(), "MMDCIX")

    def test_ASDFG(self):
        roman = GeneralisedRomanNumber("-ZASDFG")
        roman.setRomanNumber("GGGSA")
        roman.setRomanNumber("-O")
        self.assertEqual(roman.getRomanNumber(), "GGGSA")

    def test_LLA(self):
        roman = GeneralisedRomanNumber("-OALP")
        roman.setRomanNumber("LA")
        self.assertFalse(roman.setRomanNumber("LLA"))
        self.assertEqual(roman.getRomanNumber(), "LA")

    def test_SQQQVII(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRS")
        roman.setRomanNumber("SQQQVII")
        self.assertEqual(roman.getRomanNumber(), "SQQQVII")

    def test_KLO(self):
        roman = GeneralisedRomanNumber("QPOILK")
        roman.setRomanNumber("PI")
        roman.setRomanNumber("KLO")
        self.assertEqual(roman.getRomanNumber(), "KLO")

    def test_IVXLCDMPQRSTUWY_t(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
        roman.setRomanNumber("YWUSSSRMMMXLVI")
        self.assertEqual(roman.getRomanNumber(), "YWUSSSRMMMXLVI")

    # Wrong roman number
    def test_WrongNumber(self):
        roman = GeneralisedRomanNumber("-OIVXLCDM")
        roman.setRomanNumber("MMDXXL")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IV_IVI(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("IVI")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IV_IVV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("IVV")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IV_VV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("VV")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_VX(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("VX")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IXV(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWYZEFGH")
        roman.setRomanNumber("IXV")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_CMMMXCIX(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("CMMMXCIX")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_MIVIVIII(self):
        roman = GeneralisedRomanNumber()
        roman.setRomanNumber("MIVIVIII")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_RR(self):
        roman = GeneralisedRomanNumber("-OIVXLCDMPQRS")
        roman.setRomanNumber("RR")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IV_VIV(self):
        roman = GeneralisedRomanNumber("-OIV")
        roman.setRomanNumber("VIV")
        self.assertEqual(roman.getRomanNumber(), "O")

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

    def test_IVX_IXV(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("IXV")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_IIX(self):
        roman = GeneralisedRomanNumber("-OIVX")
        roman.setRomanNumber("IIX")
        self.assertEqual(roman.getRomanNumber(), "O")

    def test_TestEfektivnosti(self):
        for _ in range(1000):
            roman = GeneralisedRomanNumber("-OIVXLCDMPQRSTUWY")
            roman.setValue(16353047)
            self.assertEqual(roman.getRomanNumber(), "YWUSSSRMMMXLVII")


if __name__ == "__main__":
    unittest.main()
