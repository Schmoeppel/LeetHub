class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        x_diff = abs(fx-sx)
        y_diff = abs(fy-sy)
        if x_diff < y_diff:
            min_diff = x_diff
            max_diff = y_diff
        else:
            min_diff = y_diff
            max_diff = x_diff
        return t >= min_diff + max_diff-min_diff