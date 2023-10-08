class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        if len(strs) == 1:
            return strs[0]
        for idx in range(200):
            for j, word in enumerate(strs):
                if idx >= len(word):
                    return common_prefix
                
                current_word_letter = word[idx]
                if j != 0:
                    if current_word_letter != previous_word_letter:
                        return common_prefix
                
                previous_word_letter = current_word_letter
            common_prefix += current_word_letter

