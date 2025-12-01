class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        max_product=nums[0]
        min_product=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
               max_product,min_product=min_product,max_product 
            max_product=max(max_product*n,n)
            min_product=min(min_product*n,n)
            ans=max(max_product,ans)
        return ans