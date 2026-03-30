from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        count = defaultdict(int)

        freq = [[] for _ in range(n+1)]

        for num in nums: 
            count[num]+=1
        
        for num, c in count.items(): 
            freq[c].append(num)


        res = []
        for i in range(n, 0, -1): 
            while freq[i] and k>0: 
                res.append(freq[i].pop())
                k-=1
        return res
                    



        