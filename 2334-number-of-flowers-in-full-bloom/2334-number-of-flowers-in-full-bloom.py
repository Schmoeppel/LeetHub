class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_days = []
        end_days = []
        for flower in flowers:
            start_days.append(flower[0])
            end_days.append(flower[1])

        start_days.sort()
        end_days.sort()

        #print(start_days)
        #print(end_days)

        result = [0]*len(people)
        #print(self.get_smaller_numbers(start_days, 2))

        #return [1]

        for idx, person in enumerate(people):
            started_blooming = self.get_smaller_numbers(start_days, person)
            stopped_blooming = self.get_smaller_numbers(end_days, person-1)
            #print(f"started: {started_blooming}, stopped: {stopped_blooming}, person: {person}")
            result[idx] = started_blooming - stopped_blooming

        return result
            
    def get_smaller_numbers(self, my_list, target):
        left, right = 0, len(my_list) - 1
        count = 0

        while left <= right:
            mid = (left + right) // 2

            if my_list[mid] <= target:
                count = mid + 1  # Increment the count and search the right half
                left = mid + 1
            else:
                right = mid - 1  # Search the left half

        return count

        
        
        '''max_date = 0
        for flower in flowers:
            max_date = max(max_date, flower[1])
        max_date = max(max_date, max(people))
        max_date += 1
    
        blooming_flowers = [0]*max_date
        for flower in flowers:
            for idx in range(flower[0], flower[1]+1):
                blooming_flowers[idx] += 1

        return [blooming_flowers[x] for x in people]
'''