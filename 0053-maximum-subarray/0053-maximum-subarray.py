class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        cal=0
        for i in range(len(nums)):
            cal+=nums[i]
            maxsum=max(cal,maxsum)
            if cal<0:
                cal=0
        return maxsum

                