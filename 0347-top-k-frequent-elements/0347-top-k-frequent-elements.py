class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hmap={}
        output=[]
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]]+=1
            else:
                hmap[nums[i]]=1
        for j in range(k):
            dumy=max(hmap.values())
            for key,value in hmap.items():
                if value==dumy:
                    output.append(key)
                    break
            hmap.pop(key)
        return output