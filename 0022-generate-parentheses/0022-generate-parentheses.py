class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(res,open,close,n):
            if len(res)==2*n:
                a.append(res)
            if open<n:
                backtrack(res+"(",open+1,close,n)
            if close<open:
                backtrack(res+")",open,close+1,n)
        a=[]
        backtrack("",0,0,n)
        return a