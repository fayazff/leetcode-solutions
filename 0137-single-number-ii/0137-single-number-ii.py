class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for j in range(len(nums)):
            if freq.get(nums[j])<2:
                return nums[j]