#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    number = 0
    decimal = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for numeral in reversed(roman_string):
        value = decimal.get(numeral)
        number += value if number < value * 5 else -value
    return number
