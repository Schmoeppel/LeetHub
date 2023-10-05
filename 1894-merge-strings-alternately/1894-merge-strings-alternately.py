class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        max_len = max(len1, len2)

        output = ""
        for i in range(max_len):
            if i < len1:
                output += word1[i]
            if i < len2:
                output += word2[i]

        return output
