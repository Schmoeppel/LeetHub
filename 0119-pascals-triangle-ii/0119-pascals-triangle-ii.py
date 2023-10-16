class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[x]+row[x+1] for x in range(len(row)-1)] + [1]
        return row