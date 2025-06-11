# Last updated: 6/11/2025, 1:12:58 PM
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res = []
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, node, path):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or board[r][c] not in node.children):
                return

            char = board[r][c]
            visited.add((r, c))
            node = node.children[char]
            path += char

            if node.isWord:
                res.append(path)
                node.isWord = False  # Avoid duplicates

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, path)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return res
