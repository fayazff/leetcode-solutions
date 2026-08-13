class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(value,cur):
            if len(cur)==k:
                res.append(cur[:])
                return
            for i in range(value,n+1):
                cur.append(i)
                backtrack(i+1,cur)
                cur.pop()
        
        backtrack(1,[])
        return res