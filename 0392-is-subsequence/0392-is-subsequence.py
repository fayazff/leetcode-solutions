class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True
        i,j=0,0
        while j<len(t) and i<len(s):
            if s[i]!=t[j]:
                j+=1
            elif i==len(s)-1:
                return True
            else:
                i+=1
                j+=1
        return False