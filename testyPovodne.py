from skuska import romanToInteger

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


if __name__ == "__main__":
    tests()
