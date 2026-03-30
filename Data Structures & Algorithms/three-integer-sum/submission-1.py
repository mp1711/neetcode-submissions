class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        i = 0
        res = []
        while i<n-2 and nums[i]<=0: 
            j, k = i+1, n-1
            while j<k: 
                if nums[j]+nums[k]==-nums[i]: 
                    if [nums[i],nums[j],nums[k]] not in res: 
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<-nums[i]: 
                    j+=1
                else: 
                    k-=1
            i+=1

        return res

