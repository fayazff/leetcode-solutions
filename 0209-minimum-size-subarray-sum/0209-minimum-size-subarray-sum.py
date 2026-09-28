class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        add=0
        min_count=float('inf')
        count=0
        i=0
        j=0
        
        while j<len(nums):
            add+=nums[j]

            while add >=target:
                count=j-(i-1)
                min_count=min(min_count,count)
                add=add-nums[i]
                i+=1
            j+=1
        return min_count if min_count !=float('inf') else 0

