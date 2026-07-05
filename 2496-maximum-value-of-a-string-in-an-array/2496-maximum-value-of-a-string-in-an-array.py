class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        arr=[]
        maxval=0
        for i in range(len(strs)):
            if strs[i].isalnum() and not strs[i].isdigit():
                arr.append(len(strs[i]))
            elif strs[i].isdigit():
                arr.append(int(strs[i]))
        maxval=max(arr)
        return maxval