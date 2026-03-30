class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}

        for num in nums2:
            while stack and stack[-1] < num:
                nge[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(nge.get(num, -1))

        return res