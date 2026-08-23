class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
    
        for i in range(len(nums)):
            el=(target-nums[i])
            if el in hash:
                return [hash[el],i]
            else:
                hash[nums[i]]=i
        