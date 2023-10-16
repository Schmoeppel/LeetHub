class Solution:
    def decodeString(self, s: str) -> str:
        if "[" not in s:
            return s

        for i, c in enumerate(s):
            if c == "[":
                start_idx = i
            elif c == "]":
                end_idx = i
                break

        number = s[start_idx-1]
        if start_idx-2 >= 0 and s[start_idx-2] in "0123456789":
            number = s[start_idx-2] + number
            if start_idx-3 >= 0 and s[start_idx-3] in "0123456789":
                number = s[start_idx-3] + number
        number_len = len(number)
        number = int(number)
        
        #print(number_len)
        before_content = s[:start_idx-number_len]
        content = s[start_idx+1:end_idx]
        after_content = s[end_idx+1:]

        new_string = before_content + number*content + after_content
        #print(new_string)

        return self.decodeString(new_string)