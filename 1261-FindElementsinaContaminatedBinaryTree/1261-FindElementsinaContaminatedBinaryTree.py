class FindElements:

   def __init__(self, root: Optional[TreeNode]):
       self.root = root

   def find(self, target: int) -> bool:
       country_road = []
       cur = target
       while cur:
           if cur & 1:
               cur = (cur - 1) // 2
               country_road.append(0)
           else:
               cur = (cur - 2) // 2
               country_road.append(1)
       
       take_me_home = True
       dum = self.root
       while country_road:
           direct = country_road.pop()
           if not [dum.left, dum.right][direct]:
               take_me_home = False
               break
           
           dum = [dum.left, dum.right][direct]
       
       return take_me_home