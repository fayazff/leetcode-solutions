class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if not nums:
            return []
        def backtrack(start,cur):
            res.append(cur[:])
            for i in range(start,len(nums)):
                cur.append(nums[i])
                backtrack(i+1,cur)
                cur.pop()
            


        backtrack(0,[])
        return res