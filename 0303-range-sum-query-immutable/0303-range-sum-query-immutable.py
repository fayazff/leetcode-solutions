class NumArray:

    def __init__(self, nums: List[int]):
        self.priff=[0]*len(nums)
        self.priff[0]=nums[0]
        for i in range(1,len(nums)):
            self.priff[i]=self.priff[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        ans=0
        if left>0:
            ans=self.priff[right]-self.priff[left-1]
        else:
            ans=self.priff[right]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)