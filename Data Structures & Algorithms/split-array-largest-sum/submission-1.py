class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def split(target): 
            count = 0
            s = 0
            for num in nums: 
                if num + s > target: 
                    s = 0
                    count += 1
                s+=num

            return count+1<=k
        

        l, r = max(nums), sum(nums)
        res = 0
        while l<=r: 
            m = l + (r-l)//2

            if split(m): 
                res = m
                r = m-1
            else: 
                l = m+1
        
        return res

        