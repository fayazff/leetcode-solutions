class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c  in hash:
                return [hash[c],i]
            else:
                hash[nums[i]]=i

