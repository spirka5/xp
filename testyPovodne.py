import unittest
from skuska import romanToInteger, is_number_valid

WRONG_NUMBER = -9999


def tests():
    assert romanToInteger("A", "A") == 1
    assert romanToInteger("A", "AAA") == 3
    assert romanToInteger("A", "AAAA") == -9999
    assert romanToInteger("AA", "AA") == -9999
    assert romanToInteger("A", "AXA") == -9999
    assert romanToInteger("123", "12") == -9999

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

    assert romanToInteger("IVXLCDM", "I") == 1
    assert romanToInteger("IVXLCDM", "V") == 5
    assert romanToInteger("IVXLCDM", "X") == 10
    assert romanToInteger("IVXLCDM", "L") == 50
    assert romanToInteger("IVXLCDM", "C") == 100
    assert romanToInteger("IVXLCDM", "D") == 500
    assert romanToInteger("IVXLCDM", "M") == 1000
    assert romanToInteger("IVXLCDM", "IV") == 4
    assert romanToInteger("IVXLCDM", "IX") == 9
    assert romanToInteger("IVXLCDM", "XL") == 40
    assert romanToInteger("IVXLCDM", "XC") == 90
    assert romanToInteger("IVXLCDM", "CD") == 400
    assert romanToInteger("IVXLCDM", "CM") == 900
    assert romanToInteger("IVXLCDM", "MMXIV") == 2014
    assert romanToInteger("IVXLCDM", "MMXCIX") == 2099
    assert romanToInteger("IVXLCDM", "MMIM") == -9999  # 2999  #wrong test
    assert romanToInteger("IVXLCDM", "MMCMXCIX") == 2999  # correct test

    assert romanToInteger("IVXLCDM", "MXMIV") == -9999  # 1994 # wrong test
    assert romanToInteger("IVXLCDM", "MCMXCIV") == 1994  # correct test
    assert romanToInteger("IVXLCDM", "A") == -9999
    assert romanToInteger("IVXLCDM", "IIII") == -9999
    assert romanToInteger("IVXLCDM", "VXXV") == -9999
    assert romanToInteger("IVXLCDM", "IVI") == -9999

    assert romanToInteger("IVXLCDM", "MCMXCIV") == 1994
    assert romanToInteger("IVXLCDM", "MMMCMXCIX") == 3999
    assert romanToInteger("IVXLCDM", "CDXLIV") == 444
    assert romanToInteger("IVXLCDM", "XC") == 90
    assert romanToInteger("IVXLCDM", "DCCCXC") == 890
    assert romanToInteger("IVXLCDM", "IIII") == -9999
    assert romanToInteger("IVXLCDM", "VV") == -9999
    assert romanToInteger("IVXLCDM", "IC") == -9999
    assert romanToInteger("IVXLCDM", "IL") == -9999
    assert romanToInteger("IVXLCDM", "VX") == -9999
    assert romanToInteger("IVXLCDM", "MCMC") == -9999
    assert romanToInteger("IVXLCDM", "IIV") == -9999
    assert romanToInteger("IVXLCDM", "LC") == -9999
    assert romanToInteger("IVXLCDM", "MMMM") == -9999
    assert romanToInteger("IVXLCDM", "ABC") == -9999


class MyTestCase(unittest.TestCase):
    def test_1_checkOne(self):
        self.assertEqual(1, romanToInteger("IVXLCDM", "I"))

    def test_2_checkFour(self):
        self.assertEqual(4, romanToInteger("IVXLCDM", "IV"))

    def test_3_smallCharacters(self):
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "ii"))

    def test_4_wrongNumberOrder(self):
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "IVI"))

    def test_5_checkZlyZapis(self):
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "IC"))

    def test_6_invalidInputs(self):
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "IIIIIX"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "IC"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "VX"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "XDX"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "IL"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "MMMMM"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "CMCM"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "XIC"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "XCX"))
        self.assertEqual(-9999, romanToInteger("IVXLCDM", "ICX"))

    def test_7_validInputs(self):
        self.assertEqual(14, romanToInteger("IVXLCDM", "XIV"))
        self.assertEqual(29, romanToInteger("IVXLCDM", "XXIX"))
        self.assertEqual(144, romanToInteger("IVXLCDM", "CXLIV"))
        self.assertEqual(390, romanToInteger("IVXLCDM", "CCCXC"))

    def test_8_iiv(self):
        self.assertEqual(WRONG_NUMBER, romanToInteger("IVXLCDM", "IIV"))
        self.assertEqual(WRONG_NUMBER, romanToInteger("IVXLCDM", "CCCLXL"))

    def test_9_teachersTests(self):
        self.assertEqual(romanToInteger("IVXLCDM", "MMMCMXCIX"), 3999, "Should be 3999")
        self.assertEqual(999, romanToInteger("IVXLCDM", "CMXCIX"))
        self.assertEqual(romanToInteger("IVXLCDM", "MMCDXCIX"), 2499)
        self.assertEqual(WRONG_NUMBER, romanToInteger("IVXLCDM", "LXL"))
        self.assertEqual(WRONG_NUMBER, romanToInteger("IVXLCDM", 9))
        self.assertEqual(89, romanToInteger("IVXLCDM", "LXXXIX"))

    def test_10_invalidRomanLetter(self):
        self.assertEqual(is_number_valid(" "), False)
        self.assertEqual(is_number_valid("a"), False)
        self.assertEqual(is_number_valid("!!"), False)
        self.assertEqual(is_number_valid("ABB"), False)
        self.assertEqual(is_number_valid("OOJ"), False)
        self.assertEqual(is_number_valid(2), False)

    def test_11_invalidRomanLetter(self):
        self.assertEqual(is_number_valid("A"), True)
        self.assertEqual(is_number_valid("IXY"), True)
        self.assertEqual(is_number_valid("ABC"), True)
        self.assertEqual(is_number_valid("YURE"), True)

    def test_13_teachersTest2(self):
        self.assertEqual(romanToInteger("IV", "VIII"), 8)
        self.assertEqual(romanToInteger("A", "AAA"), 3)
        self.assertEqual(romanToInteger("I", "IV"), -9999)
        self.assertEqual(romanToInteger("IVXL", "LXXXIX"), 89)
        self.assertEqual(romanToInteger("IAVXLCQDM", "QVA"), 1015)
        self.assertEqual(romanToInteger("IVXLCDMPQRS", "SSS"), 300000)
        self.assertEqual(romanToInteger("'", "IV"), -9999)
        self.assertEqual(romanToInteger("IVXLX", "IV"), -9999)
        self.assertEqual(romanToInteger("IV", ""), -9999)
        self.assertEqual(romanToInteger("12345", "12"), -9999)


if __name__ == "__main__":
    tests()
    unittest.main()
