class Solution:
    def numberToWords(self, num: int) -> str:
        digit_name = "Zero One Two Three Four Five Six Seven Eight Nine".split()
        tens_name = "* * Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        teens_name = "Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        
        out = ""
        if billions := num // 1_000_000_000:
            out += self.numberToWords(billions) + " Billion "
        if millions := (num // 1_000_000) % 1000:
            out += self.numberToWords(millions) + " Million "
        if thousands := (num // 1000) % 1000:
            out += self.numberToWords(thousands) + " Thousand "
        if hundreds := (num // 100) % 10:
            out += digit_name[hundreds] + " Hundred "
        if (tens := (num // 10) % 10) > 1:
            out += tens_name[tens] + " "
        if tens == 1:
            out += teens_name[num % 10] + " "
        elif num % 10 or not out:
            out += digit_name[num % 10] + " "

        return out[:-1]
.