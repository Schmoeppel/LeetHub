class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        length = len(s)
        rows = numRows
        row = 0
        idx = 0
        direction = -1

        strings = [""]*rows
        
        while idx < length:
            if row == 0 or row == rows-1:
                direction = -direction
            strings[row] += s[idx]
            row += direction
            idx += 1

        result = ""
        for i in range(rows):
            result += strings[i]

        return result