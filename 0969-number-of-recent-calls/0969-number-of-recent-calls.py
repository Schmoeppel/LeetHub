class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        idx = 0
        while idx < len(self.calls):
            if t-self.calls[idx] > 3000:
                self.calls.pop(idx)
            else:
                break
        return len(self.calls)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)