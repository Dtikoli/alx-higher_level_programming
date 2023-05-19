#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    number = 0
    decimal = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    value_list = [decimal.get(numeral, 0) for numeral in reversed(roman_string)]
    for value in value_list:
        number += value if number < 5 * value else -value
    return number
