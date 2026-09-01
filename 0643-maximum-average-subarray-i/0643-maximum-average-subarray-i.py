class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxsum=summ
        i=k
        while i<len(nums):
            summ=summ-nums[i-k]+nums[i]
            maxsum=max(maxsum,summ)
            i+=1
        return maxsum/k