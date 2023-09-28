class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r_pointer = 0
        len_s = len(s)
        max_len = 0

        substring = []

        while r_pointer < len_s:
            if s[r_pointer] not in substring:
                substring.append(s[r_pointer])
                max_len = max(max_len, len(substring))
                r_pointer += 1
            else:
                substring.pop(0)
        
        return max_len
            
