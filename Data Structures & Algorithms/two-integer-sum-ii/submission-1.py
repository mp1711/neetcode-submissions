class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers)-1

        while i<j: 
            l, r = numbers[i], numbers[j]
            if l+r==target: 
                return [i+1, j+1]
            elif l+r>target: 
                j-=1
            else: 
                i+=1
        
        return 
        