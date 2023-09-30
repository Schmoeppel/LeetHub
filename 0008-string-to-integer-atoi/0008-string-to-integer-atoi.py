class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        length = len(s)
        negative = False
        result = 0
        result_string = ''

        digits = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }

        if length <= 0:
            return 0

        while True:
            if i >= length:
                return 0
            elif s[i] == ' ':
                i += 1
            else:
                break

        
        
        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == '+':
            i += 1

        while True:
            if i >= len(s):
                break
            elif s[i] in digits:
                result_string += s[i]
                i += 1            
            else:
                break
        
        pot = 0
        for i in range(len(result_string)-1, -1, -1):
            result += digits[result_string[i]] * 10**pot
            pot += 1
        
        if negative == True:
            result = -result

        max_value = 2**31-1
        min_value = -2**31
        result = max(min(result, max_value), min_value)


        return result
        
