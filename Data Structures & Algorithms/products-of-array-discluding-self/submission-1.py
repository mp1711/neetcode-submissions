class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]

        temp = 1
        for i in range(n - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]

        return res