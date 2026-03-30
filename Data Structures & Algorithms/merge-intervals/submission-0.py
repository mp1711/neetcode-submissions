from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0]
        res = []

        for st, ed in intervals[1:]:

            if st <= end:
                end = max(end, ed)
            else:
                res.append([start, end])
                start = st
                end = ed

        res.append([start, end])

        return res