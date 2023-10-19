class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        idx = 0
        while idx < len(s):
            if s[idx] == "#":
                if idx == 0:
                    s = s[1:]
                else:
                    s = s[:(idx-1)] + s[(idx+1):]
                    idx -= 1
            else:
                idx += 1

        idx = 0
        while idx < len(t):
            if t[idx] == "#":
                if idx == 0:
                    t = t[1:]
                else:
                    t = t[:(idx-1)] + t[(idx+1):]
                    idx -= 1
            else:
                idx += 1

        return s == t

