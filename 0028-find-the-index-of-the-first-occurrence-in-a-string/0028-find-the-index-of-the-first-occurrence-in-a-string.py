class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or not haystack:
            return -1
        n=len(needle)
        m=len(haystack)
        for i in range(m-n+1):
            if haystack[i:n+i]==needle:
                return i
        return -1