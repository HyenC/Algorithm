class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if (s_dict[char] != top):
                        return False
                else:
                    return False
        if stack:
            return False
        return True