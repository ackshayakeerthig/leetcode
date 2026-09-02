class SmallestInfiniteSet:

    def __init__(self):
        self.h=[i for i in range(1,1001)]
        heapq.heapify(self.h)
        self.st={i for i in range(1,1001)}
    def popSmallest(self) -> int:
        ans=heapq.heappop(self.h)
        self.st.remove(ans)
        return ans

    def addBack(self, num: int) -> None:
        if num in self.st:
                return
        self.st.add(num)
        heapq.heappush(self.h,num)
        return 
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)