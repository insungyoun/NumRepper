# This is NumRepper. It's designed by moi, Insung Youn!
# I designed this

# All inputs for converter methods are string-formatted number representation.
# Dictionary for hexadecimal conversion
hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
              '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
              'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

# Dictionary for remainder conversion
remainder_to_hex = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
                    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                    '10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}


# method to convert binary number to decimal number
def binary_to_decimal(start: str) -> str:
    start_rev = start[::-1]  # reverse input binary string
    res = 0  # store resulting decimal int value
    for i in range(len(start_rev)):  # iterate through the reversed digits of the binary input
        res += int(start_rev[i]) * (2**i)  # sum up the product of the base^index and its respective binary digit
    return str(res)  # return the sum in string form


# method to convert octal number to decimal number
def octal_to_decimal(start: str) -> str:
    start_rev = start[::-1]
    res = 0
    for i in range(len(start_rev)):
        res += int(start_rev[i]) * (8**i)
    return str(res)


# method to convert hexadecimal number to decimal number
def hexadecimal_to_decimal(start: str) -> str:
    start_rev = start[::-1]
    res = 0
    for i in range(len(start_rev)):
        res += int(binary_to_decimal(hex_to_bin[start_rev.lower()[i]])) * (16**i)
    return str(res)


# method to convert decimal number to binary number
def decimal_to_binary(start: str) -> str:
    curr_dec = int(start)  # stores current quotient in conversion
    result_bin_rev = ''  # stores reversed binary result
    while curr_dec != 0:  # loop modifies curr_dec value
        result_bin_rev = result_bin_rev + str(curr_dec % 2)
        curr_dec = curr_dec // 2
    return result_bin_rev[::-1]  # returns forward-reading binary string


# method to convert decimal number to octal number
def decimal_to_octal(start: str) -> str:
    curr_dec = int(start)
    result_oct_rev = ''
    while curr_dec != 0:
        result_oct_rev = result_oct_rev + str(curr_dec % 8)
        curr_dec = curr_dec // 8
    return result_oct_rev[::-1]


# method to convert decimal number to hexadecimal number
def decimal_to_hexadecimal(start: str) -> str:
    curr_dec = int(start)
    result_hex_rev = ''
    while curr_dec != 0:
        result_hex_rev = result_hex_rev + remainder_to_hex[str(curr_dec % 16)]
        curr_dec = curr_dec // 16
    return result_hex_rev[::-1]


allowed_dig_decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
allowed_dig_binary = ['0', '1']
allowed_dig_octal = ['0', '1', '2', '3', '4', '5', '6', '7']
allowed_dig_hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

# Main
print("Welcome to Insung's NumRepper!")
while True:
    start_base = input("Please enter desired starting base for conversion(decimal, binary, octal, hexadecimal)\n")
    while start_base not in ['decimal', 'binary', 'octal', 'hexadecimal']:
        start_base = input("Not a valid base. Please enter base.\n")

    start_num = input("Please enter desired starting number (in base {})\n".format(start_base))
    start_num = start_num.lower()


    def validation(sn: str):
        count = 0
        for ch in sn:
            if ch not in eval('allowed_dig_' + '{}'.format(start_base)):
                count += 1
            else:
                pass
        return count == 0


    while not validation(start_num):
        start_num = input(f"Not a valid {start_base} number. Please enter number again.\n")

    result_base = input("Please enter desired resulting base for conversion(decimal, binary, octal, hexadecimal)\n")
    while result_base not in ['decimal', 'binary', 'octal', 'hexadecimal']:
        result_base = input("Not a valid base. Please enter base.\n")


    def main_converter(sb: str, sn: str, rb: str):
        if sb == rb:
            return sn
        else:
            if sb != 'decimal' and rb != 'decimal':
                if sb == 'binary':
                    if rb == 'octal':
                        return decimal_to_octal(binary_to_decimal(sn))
                    elif rb == 'hexadecimal':
                        return decimal_to_hexadecimal(binary_to_decimal(sn))
                elif sb == 'octal':
                    if rb == 'binary':
                        return decimal_to_binary(octal_to_decimal(sn))
                    elif rb == 'hexadecimal':
                        return decimal_to_hexadecimal(octal_to_decimal(sn))
                elif sb == 'hexadecimal':
                    if rb == 'binary':
                        return decimal_to_binary(hexadecimal_to_decimal(sn))
                    elif rb == 'octal':
                        return decimal_to_octal(hexadecimal_to_decimal(sn))
            else:
                return eval(start_base + '_to_' + result_base + '({})'.format(start_num))


    print(f"{start_base} number {start_num} in {result_base} is {main_converter(start_base, start_num, result_base)}")
