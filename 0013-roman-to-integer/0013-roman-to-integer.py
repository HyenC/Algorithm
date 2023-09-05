class Solution:
    def romanToInt(self, s: str) -> int:
        num = {
            'I' : '1a',
            'V' : '5a',
            'X' : '10a',
            'L' : '50a',
            'C' : '100a',
            'D' : '500a',
            'M' : '1000a',
            'CM' : '900a',
            'CD' : '400a',
            'XC' : '90a',
            'XL' : '40a',
            'IX' : '9a',
            'IV' : '4a'
        }
        for r in reversed(num):
            s = s.replace(r, num[r])
        return sum(map(int, s.split('a')[:-1]))