class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """

        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while right<len(nums):
           
            if nums[right]!=0:
                dumy=nums[left]
                nums[left]=nums[right]
                nums[right]=dumy
                right+=1
                left+=1
            else:
                right+=1
