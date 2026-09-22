class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set=set(nums)
        output=0
        for i in nums_set:
            if i-1 not in nums_set:
                current=i
                lenght=1
                while current+1 in nums_set:
                    lenght+=1
                    current+=1
                output=max(output,lenght)
        return output
                

