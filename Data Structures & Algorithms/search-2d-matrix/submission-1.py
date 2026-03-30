class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        cl, cr = 0, len(matrix)-1
        rl, rr = 0, len(matrix[0])-1

        while cl<=cr: 
            cm = (cl+cr)//2

            if matrix[cm][0]<=target: 
                cl = cm+1
            else: 
                cr = cm-1
        
        nums = matrix[cr]

        while rl<=rr: 

            rm = (rl+rr)//2
            print(cm, rl, rr, rm)

            if nums[rm]==target: 
                return True
            elif target>nums[rm]: 
                rl = rm+1
            else: 
                rr = rm-1
        
        return False

        