class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pointer1 = 0
        pointer2 = 0

        cur_val = 0
        last_val = 0

        length1 = len(nums1)
        length2 = len(nums2)
        while pointer1 < length1 or pointer2 < length2:
            last_val = cur_val
            if pointer1 >= length1:
                cur_val = nums2[pointer2]
                pointer2 += 1
            elif pointer2 >= length2:
                cur_val = nums1[pointer1]
                pointer1 += 1
            elif nums1[pointer1] < nums2[pointer2]:
                cur_val = nums1[pointer1]
                pointer1 += 1
            else:
                cur_val = nums2[pointer2]
                pointer2 += 1

            if pointer1+pointer2 > (length1 + length2)/2:
                break
            
        if (length1+length2) % 2 == 1:
            return cur_val
        else:
            return (cur_val+last_val)/2