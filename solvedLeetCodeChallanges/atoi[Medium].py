# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

def myAtoi(self, str: str) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -1*(2**31)
        is_neg = False
        number = ""
        final = 0

        for i in range(len(str)):

            if str[i] == ' ':
                continue

            if str[i] == '-' or str[i] == '+' or str[i].isdigit():
                try:
                        if str[i+1] == '-' or str[i+1] == '+' or str[i+1].isalpha() or str[i+1] == ' ' or str[i+1] == '.':
                            number += str[i]
                            break
                        else:
                            number += str[i]
                            continue
                except IndexError:
                    if str[i].isdigit():
                        number += str[i]
                        continue
            if str[i].isalpha and len(number) <= 0:
                return 0



        if len(number) == 0:
            return 0

        if number[0] == '+' or number[0] == '-':
            if number[0] == '+':
                is_neg = False
            elif number[0] == '-':
                is_neg = True
            number = number[1::]

        if len(number) == 0:
            return 0

        pwr = len(number) - 1

        for digit in number:
            digitVal = ord(digit) - ord('0')
            final += digitVal * (10 ** pwr)
            pwr -= 1


        if final > INT_MAX:
            if is_neg:
                return INT_MIN
            else:
                return INT_MAX

        if is_neg:
            return -1*final
        else:
            return final
