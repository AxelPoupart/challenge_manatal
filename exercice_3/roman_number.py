

def convert_to_roman(N):
    return recur_roman(N, 0)


roman_numbers = [{'ones': 'I', 'five': 'V'}, {'ones': 'X', 'five': 'L'}, {
    'ones': 'C', 'five': 'D'}, {
    'ones': 'M', 'five': 'V'}]


def recur_roman(N, rank):
    M = N//10
    K = N % 10

    if K == 9:
        rom = roman_numbers[rank % 4]['ones'] + \
            roman_numbers[(rank+1) % 4]['ones']
    elif K == 4:
        rom = roman_numbers[rank % 4]['ones'] + roman_numbers[rank % 4]['five']
    else:
        rom = roman_numbers[rank % 4]['five'] * \
            (K//5) + roman_numbers[rank % 4]['ones']*(K % 5)

    if M == 0:
        return rom
    else:
        return recur_roman(M, rank+1) + rom


print(convert_to_roman(5))
print(convert_to_roman(4))
print(convert_to_roman(14))
print(convert_to_roman(99))
print(convert_to_roman(398))
print(convert_to_roman(984))
print(convert_to_roman(4498))
print(convert_to_roman(45498))
print(convert_to_roman(93498))
print(convert_to_roman(6666666))

# ANSWERS
# V
# IV
# XIV
# XCIX
# CCCXCVIII
# CMLXXXIV
# MVCDXCVIII
# IVVCDXCVIII
# IXMMMCDXCVIII
# DCLXVIVMDCLXVI

# Not really sure if what happened after 8999 is true in latin but this way is funny (not really sur that 4000 is VM too)
