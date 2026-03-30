class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        left, right = height[l], height[r]
        res = 0
        while l<r: 
            if left<right: 
                l+=1
                left = max(left, height[l])
                res += left - height[l]
            else: 
                r-=1
                right = max(right, height[r])
                res += right - height[r]
        
        return res


