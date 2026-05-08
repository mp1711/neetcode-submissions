class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a, b, c, = target

        founda = foundb = foundc = False

        for i, j, k in triplets: 

            if i>a or j>b or k>c: 
                continue
            if a==i: 
                founda = True
            if b==j: 
                foundb = True
            if c==k: 
                foundc = True
        
        return founda and foundb and foundc

        