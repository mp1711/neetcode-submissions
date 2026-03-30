class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals or len(intervals)==0: 
            return [newInterval]

        start, end = newInterval
        insertionindex = 0
        for i in range(len(intervals)): 
            if start<intervals[i][0]: 
                insertionindex = i
                break
            insertionindex = i+1
        
        intervals.insert(insertionindex, newInterval)


        res = []
        start, end = intervals[0]

        for st, ed in intervals[1:]: 
            if st<=end: 
                end = max(end, ed)
                start = min(start, st)
            else: 
                res.append([start, end])
                start = st
                end = ed
        
        res.append([start, end])

        return res



        