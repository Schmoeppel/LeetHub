class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        
        dic = {}

        for num in arr:
            one_count = bin(num).count('1')
            if one_count in dic:
                dic[one_count].append(num)
            else:
                dic[one_count] = [num]

        keys = list(dic.keys())
        
        keys.sort()
        result = []
        for key in keys:
            result += dic[key]

        return result