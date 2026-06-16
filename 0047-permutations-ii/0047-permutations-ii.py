from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms=list(permutations(nums))
        sets=set(perms)
        ans=list(sets)
        return ans