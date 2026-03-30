from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = deque()
        n = len(nums)
        r = 0

        while r<n: 

            while q and nums[q[-1]]<nums[r]: 
                q.pop()
            q.append(r)

            if r>=k-1: 
                while q[0]<=r-k:
                    q.popleft()
                res.append(nums[q[0]])
                    
            r+=1
        
        return res



     