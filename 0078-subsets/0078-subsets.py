class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #result=[]
        #sub=[]
        #def dfs(i):
         #   if i>=len(nums):
          #      result.append(sub.copy())
           #     return 
        #include nums[i]
            #sub.append(nums[i])
            #dfs(i+1)
        #not include nums[i]
            #sub.pop()
            #dfs(i+1)
        #dfs(0)           
        #return result
        res=[]
        def backtrack(start,cur):
            res.append(cur[:])
            for i in range(start,len(nums)):
                cur.append(nums[i])
                backtrack(i+1,cur)
                cur.pop()
        backtrack(0,[])
        return res