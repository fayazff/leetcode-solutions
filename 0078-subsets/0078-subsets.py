class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(cur,sub):
            res.append(sub[:])
            for i in range(cur,len(nums)):
                sub.append(nums[i])
                backtrack(i+1,sub)
                sub.pop()



        backtrack(0,[])
        return res