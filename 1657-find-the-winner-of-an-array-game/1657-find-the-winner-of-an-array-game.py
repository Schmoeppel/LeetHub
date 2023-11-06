class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        cnt = 0
        winner = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                return winner
        
        return winner