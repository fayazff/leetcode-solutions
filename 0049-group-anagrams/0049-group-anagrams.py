class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        s = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in s:
                s[key] = []

            s[key].append(word)

        return list(s.values())


        