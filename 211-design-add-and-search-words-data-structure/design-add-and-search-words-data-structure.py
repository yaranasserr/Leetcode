class TrieNode:
    def __init__(self):
        self.children = {}  # Fixed typo
        self.endofword = False  # Consistent naming style


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root  # current character
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # inserting characters
            cur = cur.children[c]  # char already exists

        cur.endofword = True  # Mark end of word

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # recursive case for wildcard
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endofword

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
