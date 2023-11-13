class Solution:
    def sortVowels(self, s: str) -> str:

        def sort_string(unsorted_str):
            unsorted_str = [ord(char) for char in unsorted_str]
            unsorted_str.sort()
            sorted_str = ""
            for char in unsorted_str:
                sorted_str += chr(char)
            return sorted_str

        vowels = "aeiouAEIOU"

        # sort found vowels
        found_vowels = ""
        for char in s:
            if char in vowels:
                found_vowels += char

        found_vowels = sort_string(found_vowels)

        # replace vowels in string
        vowel_idx = 0
        for i, char in enumerate(s):
            if char in vowels:
                s = s[:i] + found_vowels[vowel_idx] + s[i+1:]
                vowel_idx += 1

        return s