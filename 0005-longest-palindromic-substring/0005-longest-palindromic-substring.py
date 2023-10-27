class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
            return s

        def get_longest_palindrome(s, idx, left, right):
            while left > -1 and right < length:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            #print(f"left: {left}, right: {right}")
            palindrome = s[left+1:right]
            #print(palindrome)
            return palindrome

        max_palindrome = ""
        for idx in range(length):
            left_idx = idx-1
            right_idx = idx

            palindrome = get_longest_palindrome(s, idx, left_idx, right_idx)
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome

            left_idx = idx-1
            right_idx = idx+1

            palindrome = get_longest_palindrome(s, idx, left_idx, right_idx)
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome

        return max_palindrome

    
        
            
                    

