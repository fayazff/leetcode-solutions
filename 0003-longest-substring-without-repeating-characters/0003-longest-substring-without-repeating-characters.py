class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mac=set()
        left=0
        ans=0
        for right in range(len(s)):
            while s[right] in mac:
                mac.remove(s[left])
                left+=1
            mac.add(s[right])
            ans=max(ans,right-left+1)
        return ans