# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s= list(s)
#         res= []
#         for char in s :
#             if char == "-":
#                 res.append("-")
#             if char == "0" or char == " ":
#                 continue 
#             if not char.isdigit():
#                 break 
#             else:
#                 res.append(char)

#         print(res)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s.lstrip())  # Convert to list and remove leading whitespace
        if not s:
            return 0
        
        res = []
        sign = 1

        if s[0] == "-":
            sign = -1
            s.pop(0)
        elif s[0] == "+":
            s.pop(0)

        for char in s:
            if not char.isdigit():
                break
            res.append(char)

        if not res:
            return 0

        num = int("".join(res)) * sign

        # Clamp to 32-bit integer range
        int_min, int_max = -2**31, 2**31 - 1
        return max(min(num, int_max), int_min)
