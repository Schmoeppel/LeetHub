class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        height = 0

        for g in gain:
            height += g
            max_height = max(height, max_height)

        return max_height