"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1- deep copy of the nodes 
        # hashmap : map original node to new node 
        oldtocopy ={None:None} # oldnode : copy of node
        # if cur.next is null : edge case 
        cur = head 
        while cur :
            copy = Node(cur.val)
            oldtocopy[cur] = copy 
            cur = cur.next 

        # 2- connect the nodes 
        cur = head 
        while cur :
            copy = oldtocopy[cur] # copy node 
            # set pointers for copy node
            copy.next = oldtocopy[cur.next]
            copy.random =oldtocopy[cur.random]
            cur = cur.next

        return oldtocopy[head]


        