class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        i = 0
        n = len(tokens)
        stack = []

        while i<n: 
            if tokens[i].isnumeric() or tokens[i][1:].isnumeric(): 
                stack.append(tokens[i])
            else: 
                a, b = int(stack.pop()), int(stack.pop())
                if tokens[i]=="+": 
                    stack.append(a+b)
                elif tokens[i]=="-": 
                    stack.append(b-a)
                elif tokens[i]=="*": 
                    stack.append(a*b)
                else: 
                    stack.append(b/a)
            i+=1
        
        return int(stack[-1])

        