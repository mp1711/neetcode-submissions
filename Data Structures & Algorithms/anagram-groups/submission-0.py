from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for st in strs: 
            count = [0]*26

            for s in st:
                count[ord(s)-97] += 1

            res[tuple(count)].append(st)
        
        return list(res.values())
            
