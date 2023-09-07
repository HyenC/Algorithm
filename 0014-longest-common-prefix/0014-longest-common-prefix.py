class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort(key=lambda x : len(x))
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if strs[0][i] != s[i]:
                    return strs[0][:i]

        return strs[0]