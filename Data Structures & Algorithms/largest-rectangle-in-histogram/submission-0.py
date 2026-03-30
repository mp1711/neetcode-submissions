class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                ind, val = stack.pop()
                maxarea = max(maxarea, val * (i - ind))
                start = ind   

            stack.append([start, h])

        n = len(heights)

        for ind, val in stack:
            maxarea = max(maxarea, val * (n - ind))

        return maxarea
