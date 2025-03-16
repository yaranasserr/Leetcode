class Solution(object):
    def intToRoman(self, num):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman = []
        for val , sym in values :
            if num// val : 
                count = num//val # thousand  # 3749 // 1000 = 3 
                roman += (sym*count) 
                num = num % val # # 3749 % 1000 = 749

        return "".join(roman)
# class Solution(object):
#     def intToRoman(self, num):
#         values = {
#             1: "I",
#             4: "IV",
#             5: "V",
#             9: "IX",
#             10: "X",
#             40: "XL",
#             50: "L",
#             90: "XC",
#             100: "C",
#             400: "CD",
#             500: "D",
#             900: "CM",
#             1000: "M"
#         }

#         thousand = (num // 1000) * 1000 if num >= 1000 else 0
#         hundred = ((num % 1000) // 100) * 100 if num >= 100 else 0
#         tenth = ((num % 100) // 10) * 10 if num >= 10 else 0
#         unit = num % 10

#         res = []
#         if thousand: res.append([thousand // 1000, 1000])
#         if hundred: res.append([hundred // 100, 100])
#         if tenth: res.append([tenth // 10, 10])
#         if unit: res.append([unit, 1])

#         roman = []

#         for a, b in res:
#             if a <= 3:
#                 roman.append(a * values[b])
#             elif a == 4:
#                 roman.append(values[b * 4])
#             elif a == 5:
#                 roman.append(values[b * 5])
#             elif 6 <= a <= 8:
#                 roman.append(values[b * 5] + (a - 5) * values[b])
#             elif a == 9:
#                 roman.append(values[b] + values[b * 10])

#         return "".join(roman)
