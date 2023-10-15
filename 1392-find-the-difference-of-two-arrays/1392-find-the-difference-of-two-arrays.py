class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = nums1.copy()
        res2 = nums2.copy()
        for num in set(nums1):
            if num in nums2:
                res1 = [x for x in res1 if x != num]
                res2 = [x for x in res2 if x != num]
            
                
        return [set(res1),set(res2)]