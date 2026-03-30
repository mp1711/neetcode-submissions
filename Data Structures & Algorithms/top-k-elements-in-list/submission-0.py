from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count, freq = defaultdict(int), [[] for i in range(len(nums)+1)]

        for n in nums: 
            count[n]+=1
        
        for n, c in count.items(): 
            freq[c].append(n)
        

        res = []

        while k>0: 
            for i in range(len(freq)-1, 0, -1): 
                for n in freq[i]: 
                    if k>0: 
                        res.append(n)
                        k-=1
        return res


        