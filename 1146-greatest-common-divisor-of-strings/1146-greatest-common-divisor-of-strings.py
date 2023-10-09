class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            short_str = str2
        else:
            short_str = str1

        x = ""
        result = ""
        for char in short_str:
            x += char
            if str1.replace(x, "") == "" and str2.replace(x, "") == "":
                result = x
        
        return result
            
