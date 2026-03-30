class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        l = 0; r = n-1
        found = False

        while l<=r: 
            m = l + (r-l)//2
            if nums[m]==target: 
                found = True
                break
            elif target > nums[m]: 
                l = m+1
                while l<n-1 and nums[l]==nums[l-1]: 
                    l+=1
            else: 
                r = m-1
                while r>0 and nums[r]==nums[r+1]:
                    r-=1

        if not found: 
            return [-1, -1]

        start, end = m, m
        while start>0 and nums[start-1]==nums[start]: 
            start-=1
        while end<n-1 and nums[end]==nums[end+1]: 
            end+=1
        
        return [start, end]
        