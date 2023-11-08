class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        length = len(potions)
        result = [0]*len(spells)
        #print("----")

        for i, spell in enumerate(spells):
            searched_potion = math.ceil(success/spell)
            #print(f"searched: {searched_potion}")

            left, right = 0, length-1

            while left<=right:
                mid = left + (right-left)//2
                if potions[mid] < searched_potion:
                    left = mid+1
                else:
                    right = mid-1
            #print(left)
            
            result[i] = length-left

        return result