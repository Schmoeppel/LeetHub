class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        string = str(abs(x))

        reverse_string = ""
        for char in string:
            reverse_string = char + reverse_string

        res = int(int(reverse_string) * sign)
        if res > 2**31-1 or res < -2**31:
            res = 0
        return res

