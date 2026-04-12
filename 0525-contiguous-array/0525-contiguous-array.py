class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
         
        output=0
        add=0
        hashmap={}
        for i in range(len(nums)):
                if nums[i] == 0:
                    add-=1
                else:
                    add+=1
                if add ==0:
                    output=max(output,i+1)
                elif add in hashmap:
                    output=max(output,i-hashmap[add])
                else:
                    hashmap[add]=i
        return output
