class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]  # [L3] collect all permutations here
        if len(nums)==1: # [L4] only one element? only one permutation
            return[nums[:]] # [L5] return [[that_element]]; .copy() avoids aliasing

        for i in range(len(nums)): # [L7] give each element a turn to be appended last
            n=nums.pop(0)  # [L8] remove the first element (rotating the list)
            perms=self.permute(nums)  # [L9] get all perms of the remaining elements

            for perm in perms: # [L11] for every smaller permutation...
                perm.append(n) # [L12] ...attach the popped n at the end

            result.extend(perms)  # [L14] dump those new permutations into result
            nums.append(n) # [L15] restore n to nums (so the list rotates for next loop)
        return result  # [L17] done: all permutations accumulated