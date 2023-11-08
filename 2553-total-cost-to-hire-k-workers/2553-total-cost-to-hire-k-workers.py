class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_idx = candidates
        right_idx = len(costs)-candidates

        left_heap = costs[:left_idx]
        right_heap = costs[right_idx:]

        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        total_cost = 0

        #print(left_heap)
        #print(right_heap)

        hires = []

        remaining_sessions = 0
        overlap = False
        for i in range(k):
            if left_idx > right_idx:
                overlap = True
                #print("overlap")
                remaining_sessions = k
                break
            
            #print(f"left min: {left_heap[0]}, right min: {right_heap[0]}")
            #print(f"left: {left_idx}, right: {right_idx}")
            if left_heap[0] <= right_heap[0]:
                if left_idx == right_idx:
                    remaining_sessions = k-i
                    break
                hires.append(left_heap[0])
                total_cost += heapq.heappop(left_heap)
                #print(f"add left: {costs[left_idx]}")
                heapq.heappush(left_heap, costs[left_idx])
                #print(f"new left heap: {left_heap}")
                left_idx += 1
            else:
                if left_idx == right_idx:
                    remaining_sessions = k-i
                    break
                hires.append(right_heap[0])
                total_cost += heapq.heappop(right_heap)
                #print(f"add right: {costs[right_idx]}")
                right_idx -= 1
                heapq.heappush(right_heap, costs[right_idx])
                #print(f"new right heap: {right_heap}")
                

        if remaining_sessions:
            if overlap:
                left_heap = costs
                heapq.heapify(left_heap)
            else:
                #print(f"left before merge: {left_heap}")
                #print(f"right before merge: {right_heap}")
                left_heap.extend(right_heap)
                heapq.heapify(left_heap)
            for i in range(remaining_sessions):
                hires.append(left_heap[0])
                total_cost += heapq.heappop(left_heap)

        #print(f"hires: {hires}")
        return total_cost

            