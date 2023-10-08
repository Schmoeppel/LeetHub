class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_value = 0
        for idx, char in enumerate(s):
            value = symbol_to_value[char]
            
            next_char = ''
            if idx < len(s)-1:
                next_char = s[idx+1]

            if char+next_char in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                value = -value

            total_value += value
        
        return total_value
