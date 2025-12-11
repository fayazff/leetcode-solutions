class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def calling(res,open,close,n):
            if len(res)==2*n:
                a.append(res)
            if open<n:
                calling(res+"(",open+1,close,n)
            if close<open:
                calling(res+")",open,close+1,n)
        a=[]
        calling("",0,0,n)
        return a