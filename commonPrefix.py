class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        size = len(strings)
        if size == 0:
            return ""
        if size == 1:
            return strings[0]
        strings.sort()

        end = min(len(strings[0]), len(strings[size - 1]))
        i = 0
        while i < end and strings[0][i] == strings[size - 1][i]:
            i += 1
        common_prefix = strings[0][:i]

        return common_prefix