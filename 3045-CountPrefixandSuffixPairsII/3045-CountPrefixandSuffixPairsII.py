from typing import List

# Define a TrieNode class which will represent each node in the Trie.
class TrieNode:
    def __init__(self):
        # 'children' stores the next possible (character pair) -> TrieNode mappings.
        self.children = {}
        # 'count' tracks how many words pass through or end at this node.
        self.count = 0

# Define the Trie class for managing the Trie structure and adding/counting word pairs.
class Trie: 
    def __init__(self):
        # Initialize the Trie with a root node.
        self.root = TrieNode()

    def add(self, w: str):
        """
        Adds a word to the Trie in reverse order of character pairs.
        """
        cur = self.root
        # Loop over pairs of characters in the word, reversed.
        for c1, c2 in zip(w, reversed(w)):
            # Check if the character pair (c1, c2) already exists in the current node's children.
            if (c1, c2) not in cur.children:
                # If not, create a new TrieNode for this character pair.
                cur.children[(c1, c2)] = TrieNode()
            # Move to the next node corresponding to the character pair.
            cur = cur.children[(c1, c2)]
            # Increment the count, as this word passes through this pair.
            cur.count += 1

    def count_pairs(self, w: str) -> int:
        """
        Counts how many words (added previously) have a matching prefix-suffix pair in reverse.
        """
        cur = self.root
        # Loop over pairs of characters in the word, reversed.
        for c1, c2 in zip(w, reversed(w)):
            # If the character pair (c1, c2) is not found in the current node's children, return 0.
            if (c1, c2) not in cur.children:
                return 0
            # Move to the next node corresponding to the character pair.
            cur = cur.children[(c1, c2)]
        # Return the count of how many words passed through this node.
        return cur.count

# Main Solution class to solve the problem.
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        This function counts how many pairs of words share a common prefix-suffix pair.
        """
        res = 0
        # Create an instance of the Trie to store the words and their corresponding pairs.
        trie = Trie()
        
        # Iterate through the words in reverse order (important for pairing prefix-suffix).
        for w in reversed(words):
            # Count how many previous words share a prefix-suffix pair with the current word.
            res += trie.count_pairs(w)
            # Add the current word to the Trie.
            trie.add(w)
        
        # Return the total count of prefix-suffix pairings.
        return res
