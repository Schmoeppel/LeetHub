class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        len1 = len(word1)
        len2 = len(word2)
        if len1 != len2:
            return False

        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        values1 = list(count1.values())
        values2 = list(count2.values())

        values1.sort()
        values2.sort()

        keys1 = list(count1.keys())
        keys2 = list(count2.keys())

        keys1.sort()
        keys2.sort()

        #print(keys1)
        #print(keys2)

        #print(count1)
        #print(count2)

        return values1 == values2 and keys1 == keys2