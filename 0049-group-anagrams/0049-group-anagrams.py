class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap={}
        for i in strs:
            key=tuple(sorted(i))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(i)
        return list(hashmap.values())
            