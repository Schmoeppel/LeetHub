class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        temp = list(zip(nums1, nums2))
        temp = sorted(temp, key=lambda x: x[1])
        nums1, nums2 = zip(*temp)
        nums1 = list(nums1)
        nums2 = list(nums2)
        nums1.reverse()
        nums2.reverse()

        selection = nums1[:k]
        selection_sum = sum(selection)
        heapq.heapify(selection)

        max_result = selection_sum * nums2[k-1]

        for i in range(k, len(nums1)):
            selection_sum += nums1[i] - heapq.heappushpop(selection, nums1[i])
            temp = selection_sum * nums2[i]
            max_result = max(max_result, temp)


        return max_result