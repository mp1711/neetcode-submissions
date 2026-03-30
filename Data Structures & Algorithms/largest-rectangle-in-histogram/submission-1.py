class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        res = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                ind, val = stack.pop()
                res = max(res, val * (i - ind))
                start = ind   

            stack.append([start, h])

        for ind, val in stack:
            res = max(res, val * (n - ind))

        return res
