class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        max_vowels = 0

        for i in range(k):
            if s[i] in "aeiou":
                vowels += 1

        max_vowels = vowels

        for i in range(k, len(s)):
            if s[i] in "aeiou":
                vowels += 1
            if s[i-k] in "aeiou":
                vowels -= 1
            max_vowels = max(max_vowels, vowels)

        return max_vowels

            