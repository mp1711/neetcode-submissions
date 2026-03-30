class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        i = 0
        res = []
        while i<n-2 and nums[i]<=0: 
            if i>0 and nums[i]==nums[i-1]: 
                i+=1
                continue

            j, k = i+1, n-1
            while j<k: 
                if j>i+1 and nums[j]==nums[j-1]: 
                    j+=1
                    continue
                if nums[j]+nums[k]==-nums[i]: 
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<-nums[i]: 
                    j+=1
                else: 
                    k-=1
            i+=1

        return res

