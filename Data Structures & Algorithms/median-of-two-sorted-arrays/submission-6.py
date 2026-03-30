class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2: 
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        total = n1+n2
        half = total//2


        l, r = 0, n1-1

        while True: 
            i = (l+r)//2
            j = half-(i+2)

            nl1 = nums1[i] if i>=0 else float("-inf")
            nr1 = nums1[i+1] if i+1<n1 else float("inf")
            nl2 = nums2[j] if j>=0 else float("-inf")
            nr2 = nums2[j+1] if j+1<n2 else float("inf")

            if nl1<=nr2 and nl2<=nr1: 
                if total%2: 
                    return min(nr1, nr2)
                else: 
                    return (max(nl1, nl2) + min(nr1, nr2))/2

            elif nl2>nr1:
                l = i+1
            else: 
                r = i-1

        return 0 
        