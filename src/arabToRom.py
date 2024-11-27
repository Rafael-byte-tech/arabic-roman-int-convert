def int_to_roman(num):
    if not 1 <= num <= 3999:
        return "Input must be between 1 and 3999"
    
    # Mapping of Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += symbols[i]
            num -= val[i]
        i += 1
    return roman_numeral