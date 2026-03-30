class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2: 
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)): 
            newdp = set()
            for t in dp: 
                if (t+nums[i])==target: 
                    return True
                newdp.add(t)
                newdp.add(t+nums[i])
            dp = newdp

        return True if target in dp else False

        