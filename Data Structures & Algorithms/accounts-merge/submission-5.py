from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emails = set()
        email_name = {}

        for account in accounts: 
            for email in account[1:]: 
                emails.add(email)
                email_name[email] = account[0]

        par = {email:email for email in emails}
        rank = {email:1 for email in emails}


        def find(node):
            if node!=par[node]: 
                par[node] = find(par[node]) 
            return par[node]
        
        def union(n1, n2): 
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2:
                return False
            
            if rank[p2]>rank[p1]: 
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            else: 
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            
            return True


        for account in accounts: 
            for i in range(2, len(account)): 
                union(account[i-1], account[i])

        
        groups = {}
        for email in par: 
            root = find(email)
            if root in groups: 
                groups[root].append(email)
            else: 
                groups[root] = [email]
        
        res = []
        for key, value in groups.items(): 
            res.append([email_name[key]] + value)
        
        return res



