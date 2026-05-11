class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def backtrack(i,cur: list,total):
            if len(cur)==k or total>n:
                if total==n:
                    res.append(cur[:])
                return
            for x in range(i,10):
                if x+total > n:
                    break
                cur.append(x)
                backtrack(x+1,cur,total+x)
                cur.pop()
            
        backtrack(1,[],0)
        return res