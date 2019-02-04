import sys;

def Main():
    RunTests()

def TestGraduatedValue(testName, value, decimalPlaces, addDecimalForSingleDigit, expected):
    try:
        output = graduatedValue(value, decimalPlaces, addDecimalForSingleDigit)
    except ValueError as e:
        print(e)
        output = "exception"

    if output == expected or (expected is None and output == ""):
        print ("Succeeded for " + testName)
    else:
        print ("Failed for " + testName + ": Failed with [" + ("" if output is None else output) + "] rather than [" + ("" if expected is None else expected) + "]")

def RunTests():
    TestGraduatedValue("Simplest Low Value", 123, 0, False, "123");
    TestGraduatedValue("Zero", 0, 0, False, "0");
    TestGraduatedValue("Decimal Zeros", 0, 4, False, "0.0000");

    TestGraduatedValue("Simple One Grad", 12345, 0, False, "12K");
    TestGraduatedValue("Simple With Decimals", 12345, 3, False, "12.345K");

    TestGraduatedValue("AddDec Shouldnt Affect", 12345, 0, True, "12K");
    TestGraduatedValue("Zero AddDec", 0, 0, True, "0.0");

    TestGraduatedValue("Round Integer Up", 1880, 0, False, "2K");
    TestGraduatedValue("Round Decimal Up", 1880, 1, False, "1.9K");
    TestGraduatedValue("Round After AddDec", 1880, 0, True, "1.9K");

    TestGraduatedValue("Bankers Rounding Up", 1500, 0, False, "2K");
    TestGraduatedValue("Bankers Rounding Down", 4500, 0, False, "4K");

    TestGraduatedValue("Small Negatives", -123, 0, False, "-123");
    TestGraduatedValue("Negatives", -1000, 0, False, "-1K");
    TestGraduatedValue("Negatives Bankers Up", -1500, 0, False, "-2K");
    TestGraduatedValue("Bankers Bankers Down", -4500, 0, False, "-4K");

    TestGraduatedValue("Large With Decimals", 9372036854775807, 1, True, "9.37Q");
    TestGraduatedValue("Large No More Grad", 9223372036854775807, 0, True, "9223Q");

    TestGraduatedValue("No Premature Grad", 999, 0, False, "999");
    
def graduatedValue(value, decimalPlaces, addDecimalForSingleDigit):
    def helper(_value):
        for i in range(len(listGrad)):
            if _value < listGrad[i][0]:
                i = i - 1
                break
        
        _value /= listGrad[i][0]

        if decimalPlaces == 0 and addDecimalForSingleDigit:
            if int(_value) < 10:
                return '{0:.1f}{1}'.format(_value, listGrad[i][1])
                
        return '{0:.{prec}f}{1}'.format(_value, listGrad[i][1],  prec=decimalPlaces)
    listGrad = [
        (1, ''),
        (10**3, 'K'),
        (10**6, 'M'),
        (10**9, 'B'),
        (10**12, 'T'),
        (10**15, 'Q')
    ]
    value = float(value)
    if value == 0.0:
        if decimalPlaces == 0 and addDecimalForSingleDigit:
            return '{0:.1f}'.format(value)
        return '{0:.{prec}f}'.format(value,  prec=decimalPlaces)

    elif value < 0:
        return '-' + helper(-value)
    else:
        return helper(value)

Main()