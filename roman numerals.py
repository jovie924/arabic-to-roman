arabic = int(input('enter any arabic-numeral number here (between 1 and 3999 inclusive): ')) # get integer
arabic_string = str(arabic) # make str copy of int

if arabic < 1 or arabic > 3999:
    arabic = int(input((f"it's not possible to convert {arabic} into roman numerals.\nplease try a number between 1 and 3999: ")))
else:
    # for units place
    num_digits = len(arabic_string)
    units_place = int(arabic_string[num_digits - 1])
    if units_place <= 3:
        roman_units = 'I' * units_place
    elif units_place == 4:
        roman_units = 'IV'
    elif 5 <= units_place <= 8:
        leftover_units = units_place - 5
        roman_units = 'V' + 'I' * leftover_units
    elif units_place == 9:
        roman_units = 'IX'
    elif units_place == 0:
        roman_units = ''
    
    # for tens place
    tens_place = int(arabic_string[num_digits - 2])
    if 0 < tens_place <= 3:
        roman_tens = 'X' * tens_place
    elif tens_place == 4:
        roman_tens = 'XL'
    elif 5 <= tens_place <= 8:
        leftover_tens = tens_place - 5
        roman_tens = 'L' + 'X' * leftover_tens
    elif tens_place == '9':
        roman_tens = 'XC'
    elif tens_place == 0:
        roman_tens = ''
    
    # for hundreds place
    hun_place = int(arabic_string[num_digits - 3])
    if 0 < hun_place <= 3:
        roman_huns = 'C' * hun_place
    elif hun_place == 4:
        roman_huns = 'CD'
    elif 5 <= hun_place <= 8:
        leftover_huns = hun_place - 5 
        roman_huns = 'D' + 'C' * leftover_huns
    elif hun_place == 9:
        roman_huns = 'CM'
    elif hun_place == 0:
        roman_huns = ''
    
    # for thousands place
    thou_place = int(arabic_string[num_digits - 4])
    if 0 < thou_place <= 3:
        roman_thous = 'M' * thou_place
    
if len(arabic_string) == 1:
    full_roman = roman_units    
elif len(arabic_string) == 2:
    full_roman = roman_tens + roman_units
elif len(arabic_string) == 3:
    full_roman = roman_huns + roman_tens + roman_units
elif len(arabic_string) == 4:
    full_roman = roman_thous + roman_huns + roman_tens + roman_units

print(f'{arabic} in roman numerals is {full_roman}')