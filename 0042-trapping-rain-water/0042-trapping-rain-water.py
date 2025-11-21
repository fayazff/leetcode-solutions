class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        n=len(height)
        lmax=[0]*n
        lmax[0]=height[0]
        for i in range(1,n):
            lmax[i]=max(height[i],lmax[i-1])
        rmax=[0]*n
        rmax[n-1]=height[n-1]
        for j in range(n-2,-1,-1):
            rmax[j]=max(rmax[j+1],height[j])
        for i in range(1,n-1):
            water=min(rmax[i],lmax[i])-height[i]
            if water>0:
                ans+=water
        return ans
        