class TrieNode:
    def __init__(self):
        self.children = {}  # key char : value child
        self.isword = False


    def addword(self,word):
        cur = self # root
        for c in word :
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur=cur.children[c]

        cur.isword = True  

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode ()
        for w in words :
            root.addword(w)

        rows = len(board)
        cols = len(board[0])
        res,visit = set() ,set()

        #i : current char in target word

        def dfs(r,c,node,word): 
       
            if r < 0 or c < 0 or r == rows or c==cols  or  board[r][c] not in node.children or (r,c) in visit:
                return 

            visit.add((r,c)) # CHAR IS FOUND
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)

                # Define directions for up, down, right, and left
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                # Loop through each direction and call dfs
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)

                # dfs(r+1,node,word) # up
                # dfs(r-1,c,node,word)  # down
                # dfs(r,c+1,node,word) #right
                # dfs(r,c-1,node,word)# left 

            visit.remove((r,c))
                

        for r in range(rows):
            for c in range(cols):

                dfs(r,c,root,"")

        return list(res)

        

       
            