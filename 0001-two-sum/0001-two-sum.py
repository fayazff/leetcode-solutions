class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmp={}
        for i in range(len(nums)):
            compare=target - nums[i]
            if compare in hashmp:
                return [hashmp[compare],i]
            hashmp[nums[i]]=i
            
