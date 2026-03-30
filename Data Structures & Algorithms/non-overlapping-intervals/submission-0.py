class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        remove = 0

        for st, ed in intervals[1:]:
            if st < end:
                remove += 1
            else:
                end = ed

        return remove