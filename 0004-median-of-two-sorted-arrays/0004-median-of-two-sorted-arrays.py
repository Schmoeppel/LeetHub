class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []

        pointer1 = 0
        pointer2 = 0

        length1 = len(nums1)
        length2 = len(nums2)
        while pointer1 < length1 or pointer2 < length2:
            if pointer1 >= length1:
                merged_array.append(nums2[pointer2])
                pointer2 += 1
            elif pointer2 >= length2:
                merged_array.append(nums1[pointer1])
                pointer1 += 1
            elif nums1[pointer1] < nums2[pointer2]:
                merged_array.append(nums1[pointer1])
                pointer1 += 1
            else:
                merged_array.append(nums2[pointer2])
                pointer2 += 1

            if pointer1+pointer2 > (length1 + length2)/2:
                break
            
        if (length1+length2) % 2 == 1:
            return merged_array[-1]
        else:
            return (merged_array[-1]+merged_array[-2])/2