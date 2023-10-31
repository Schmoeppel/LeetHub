class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        temp_num = 0
        for pref_num in pref:
            new_num = temp_num^pref_num
            temp_num = temp_num^new_num
            res.append(new_num)
        return res
