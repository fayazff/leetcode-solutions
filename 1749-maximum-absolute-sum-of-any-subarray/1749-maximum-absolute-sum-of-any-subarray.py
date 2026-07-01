class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pref=0
        pos=0
        neg=0
        ans=0
        for i in range(len(nums)):
            pref+=nums[i]
            ans=max(ans,abs(pref-pos),abs(pref-neg))
            if pref <0 :
                neg=min(pref,neg)
            else:
                pos=max(pref,pos)
        return ans