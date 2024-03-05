class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        integer = 0
        for i in range(len(s)):
            if i > 0 and romanDict[s[i]] > romanDict[s[i - 1]]:
                integer += romanDict[s[i]] - 2*romanDict[s[i - 1]]
            else:
                integer += romanDict[s[i]]

        return integer