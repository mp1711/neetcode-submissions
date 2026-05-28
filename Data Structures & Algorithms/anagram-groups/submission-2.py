from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = defaultdict(list)
        for s in strs: 
            asc = [0]*26
            for ch in s: 
                asc[ord(ch) - 97] += 1
            freq[tuple(asc)].append(s)
        
        return list(freq.values())

        