class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        output=[]
        pf=[1]*len(nums)
        pf[0]=nums[0]
        for i in range(1,len(nums)):
            pf[i]=pf[i-1]*nums[i]
        sf=[1]*len(nums)
        sf[n-1]=nums[n-1]
        for j in range(n-2,-1,-1):
            sf[j]=sf[j+1]*nums[j]
        for x in range(n):
            if x==0: 

                output.append(sf[1])
            elif x==n-1:
                output.append(pf[n-2])
            else:
                output.append(pf[x-1]*sf[x+1])
        return output
        