class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for ch in magazine:
            hashmap[ch] = hashmap.get(ch,0)+1
        for ch in ransomNote:
            if ch not in hashmap or hashmap[ch]==0:
                return False
            else:
                hashmap[ch]-=1
        return True
