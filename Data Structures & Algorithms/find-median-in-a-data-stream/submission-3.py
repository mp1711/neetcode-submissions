from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        if self.large and num>self.large[0]: 
            heappush(self.large, num)
        else: 
            heappush(self.small, -num)
        
        if len(self.small) > len(self.large): 
            heappush(self.large, -heappop(self.small))
        elif len(self.large) > len(self.small): 
            heappush(self.small, -heappop(self.large))
                

    def findMedian(self) -> float:
        s = len(self.small)
        l = len(self.large)
        if (s+l)%2 or s+l==1: 
            return -self.small[0] if s>l else self.large[0]
        else: 
            return (-self.small[0] + self.large[0])/2
        
        
        
        