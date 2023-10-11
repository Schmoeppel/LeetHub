class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = list(reversed(words))
        
        result = ""
        for word in words:
            if word != "":
                word = word.replace(" ", "")
                result += word + " "
        
        result = result[:-1]
        return result