# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_idx = self.find_peak_idx(mountain_arr)
        #print(peak_idx)
        target_idx = self.find_in_ascend(mountain_arr, peak_idx, target)
        #print(target_idx)
        if target_idx == -1:
            target_idx = self.find_in_descend(mountain_arr, peak_idx, target)
        return target_idx

    def find_peak_idx(self, mountain_arr):
        left = 0
        right = mountain_arr.length()-1

        while left < right:
            mid = (left+right)//2
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                right = mid
            else:
                left = mid + 1

        return mid

    def find_in_ascend(self, mountain_arr, peak, target):
        left = 0
        right = peak+1

        while left <= right:
            mid = (left+right)//2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid+1
            else:
                right = mid-1

        print(f"ascend left: {left}, right: {right}")
        '''if mountain_arr.get(left+1) == target:
            return left+1
        else:'''
        return -1

    def find_in_descend(self, mountain_arr, peak, target):
        left = peak
        right = mountain_arr.length()-1

        while left <= right:
            mid = (left+right)//2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid+1
            else:
                right = mid-1

        print(f"descend left: {left}, right: {right}")
        '''if mountain_arr.get(left+1) == target:
            return left+1
        else:'''
        return -1

    
            