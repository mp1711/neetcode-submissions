from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a, b, c = target
        found_a = found_b = found_c = False

        for i, j, k in triplets:
            if i > a or j > b or k > c:
                continue

            if i == a:
                found_a = True
            if j == b:
                found_b = True
            if k == c:
                found_c = True

            if found_a and found_b and found_c:
                return True

        return found_a and found_b and found_c