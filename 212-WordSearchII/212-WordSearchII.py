# Last updated: 6/11/2025, 1:09:30 PM
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie using dictionaries
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word  # "$" is a special marker for the end of a word

        rows, cols = len(board), len(board[0])
        res = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            next_node = node[ch]
            word_found = next_node.pop("$", None)
            if word_found:
                res.append(word_found)

            board[r][c] = "*"  # mark visited

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node:
                    backtrack(nr, nc, next_node)

            board[r][c] = ch  # restore after backtracking

            if not next_node:
                node.pop(ch)  # prune Trie

        # Step 2: Start backtracking from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    backtrack(r, c, trie)

        return res
