class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []
        for num in set(nums1):
            if num not in nums2:
                res1.append(num)

        for num in set(nums2):
            if num not in nums1:
                res2.append(num)
                
        return [res1,res2]