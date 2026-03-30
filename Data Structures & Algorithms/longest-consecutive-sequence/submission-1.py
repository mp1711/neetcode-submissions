class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numset = set(nums)

        for i in numset: 
            length = 0
            if i-1 not in numset: 
                while i+length in numset: 
                    length+=1
            longest = max(longest, length)

            length = 0
            if i+1 not in numset: 
                while i-length in numset: 
                    length+=1
            longest = max(longest, length)
        

        return longest