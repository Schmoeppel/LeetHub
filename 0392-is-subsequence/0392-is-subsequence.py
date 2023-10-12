class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True

        s_idx = 0
        for t_idx in range(len(t)):
            if s[s_idx] == t[t_idx]:
                s_idx += 1

            if s_idx == len(s):
                return True

        return False