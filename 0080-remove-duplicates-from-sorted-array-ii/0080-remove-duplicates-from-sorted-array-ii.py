class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        i=0
        j=1
        while i<=len(nums) and j<len(nums):
            if nums[i]==nums[j]:
                count+=1
                if count>2:
                    nums.pop(j)
                else:
                    j+=1
                    
            else:
                count=1
                i=j
                j+=1
        return len(nums)