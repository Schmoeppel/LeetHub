class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)

        for num in arr:
            occurrences[num] += 1

        #print(list(occurrences.values()))

        return len(set(arr)) == len(set(list(occurrences.values())))

