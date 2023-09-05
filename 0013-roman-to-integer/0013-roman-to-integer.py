class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'CM' : 900,
            'CD' : 400,
            'XC' : 90,
            'XL' : 40,
            'IX' : 9,
            'IV' : 4
        }
        total = []
        for r in reversed(num_dict):
            while r in s:
                total.append(num_dict[r])
                s = s.replace(r, '', 1)
        return sum(total)
