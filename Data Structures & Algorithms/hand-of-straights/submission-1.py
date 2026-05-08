from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        c = Counter(hand)
        total = 0
        n = len(hand)

        for num in sorted(c): 
            while c[num]>0: 
                for i in range(num, num+groupSize): 
                    if c[i]==0: 
                        return False
                    c[i]-=1
                    total+=1
            if total==n: 
                break
        
        return True



        
        
        