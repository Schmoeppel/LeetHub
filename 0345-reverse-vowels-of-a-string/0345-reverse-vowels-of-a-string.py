class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for char in s:
            if char in "aeiouAEIOU":
                vowels.append(char)

        for idx, char in enumerate(s):
            if char in "aeiouAEIOU":
                s = s[:idx] + vowels.pop() + s[idx+1:]

        return s