class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(start,cur):
            res.append(cur[:]) 
            for i in range(start,len(nums)):
                if i>start and nums[i-1]==nums[i]:
                    continue
                cur.append(nums[i])
                backtrack(i+1,cur)
                cur.pop()
        backtrack(0,[])
        return res