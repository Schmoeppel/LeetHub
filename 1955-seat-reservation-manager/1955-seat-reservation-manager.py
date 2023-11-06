class SeatManager:

    def __init__(self, n: int):
        self.empty_seats = list(range(1,n+1))
        heapq.heapify(self.empty_seats)

    def reserve(self) -> int:
        return heapq.heappop(self.empty_seats)
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.empty_seats, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)