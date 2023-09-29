class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_vol = 0

        while left != right:
            vol = (right-left) * min(height[left], height[right])
            if vol > max_vol:
                max_vol = vol
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol