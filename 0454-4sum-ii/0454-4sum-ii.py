class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count=0
        hassh={}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair_sum=nums1[i]+nums2[j]
                hassh[pair_sum]=hassh.get(pair_sum,0)+1
        for k in range(len(nums3)):
            for t in range(len(nums4)):
                pair_sum=nums3[k]+nums4[t]
                count+=hassh.get(-pair_sum,0)
                    
        return count
                