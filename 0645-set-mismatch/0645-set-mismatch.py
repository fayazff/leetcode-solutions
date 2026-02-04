class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq={}
        missing=-1
        duplicate=-1
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for i in range(1,len(nums)+1):
            if freq.get(i,0) == 2:
                duplicate=i
            elif i not in freq:
                missing=i
        return [duplicate,missing]
