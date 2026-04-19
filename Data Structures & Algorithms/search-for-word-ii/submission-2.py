class Node: 
    def __init__(self): 
        self.children = {}
        self.word = False

class Trie: 
    def __init__(self): 
        self.root = Node()
    
    def addWord(self, word): 
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for w in words: 
            trie.addWord(w)
        
        rows = len(board)
        cols = len(board[0])
        res = set()
        vis = set()
        
        def backtrack(r, c, string, node): 
            if r<0 or c<0 or r==rows or c==cols or (r, c) in vis or board[r][c] not in node.children: 
                return 
            vis.add((r, c))
            node = node.children[board[r][c]]
            string += board[r][c]
            if node.word: 
                res.add(string)
            backtrack(r+1, c, string, node)
            backtrack(r, c+1, string, node)
            backtrack(r-1, c, string, node)
            backtrack(r, c-1, string, node)
            vis.remove((r, c))
        
        for r in range(rows): 
            for c in range(cols): 
                backtrack(r, c, "", trie.root)

        return list(res)


















        