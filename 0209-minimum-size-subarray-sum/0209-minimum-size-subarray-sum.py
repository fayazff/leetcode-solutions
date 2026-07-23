class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        maxsum=0
        left=0
        res=float('inf')
        for right in range(len(nums)):
            maxsum+=nums[right]
            while maxsum >= target:
                res=min(res,right-left+1)
                maxsum = maxsum - nums[left]
                left+=1

                
        return 0 if res==float('inf') else res

