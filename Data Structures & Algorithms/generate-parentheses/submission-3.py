class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(op, cl, path): 
            if op==cl==n: 
                res.append("".join(path[:]))
                return 
            
            if op<n: 
                path.append("(")
                backtrack(op+1, cl, path)
                path.pop()
            
            if cl<op: 
                path.append(")")
                backtrack(op, cl+1, path)
                path.pop()

        backtrack(0, 0, [])

        return res
            

        