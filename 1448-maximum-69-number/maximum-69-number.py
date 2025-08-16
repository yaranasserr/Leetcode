class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = list(str(num))   # convert int -> list of chars
        for i in range(len(num_str)):
            if num_str[i] == '6':  # change first '6' to '9'
                num_str[i] = '9'
                break
        return int("".join(num_str))
