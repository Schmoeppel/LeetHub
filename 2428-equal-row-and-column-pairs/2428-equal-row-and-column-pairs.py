class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0

        transposed_grid = [[row[i] for row in grid] for i in range(len(grid[0]))]

        #print(transposed_grid)
        #print(transposed_grid[0])

        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if grid[i] == transposed_grid[j]:
                    cnt += 1

        return cnt