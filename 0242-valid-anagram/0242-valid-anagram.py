class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for chr in s:
            if chr in s_dict:
                s_dict[chr] += 1
            else:
                s_dict[chr] = 1
        
        t_dict = {}
        for chr in t:
            if chr in t_dict:
                t_dict[chr] += 1
            else:
                t_dict[chr] = 1

        return s_dict == t_dict
        