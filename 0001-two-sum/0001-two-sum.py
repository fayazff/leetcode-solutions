class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output=[]
        hmap={}
        for i in range(len(nums)):
            dumy=target-nums[i]
            if dumy in hmap:
                return [hmap[dumy],i]
            else:
                hmap[nums[i]]=i