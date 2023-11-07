class SmallestInfiniteSet:

    def __init__(self):
        self.inf_set = list(range(1,1001))

    def popSmallest(self) -> int:
        return self.inf_set.pop(0)
        

    def addBack(self, num: int) -> None:
        if num not in self.inf_set:
           # self.inf_set.append(num)
           # self.inf_set.sort()
            bisect.insort(self.inf_set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)