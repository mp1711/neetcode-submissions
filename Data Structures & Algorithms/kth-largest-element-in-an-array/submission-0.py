from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        k = len(nums)-k+1
        res = None
        while k>0: 
            res = heappop(nums)
            k-=1
        return res