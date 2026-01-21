class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        t_count={}
        for ch in t:
            t_count[ch]=t_count.get(ch,0)+1
        l=r=matches=0
        requered_count=len(t_count)
        ans_len=float("inf")
        window_count={}
        ans_l=0
        ans_r=0
        while r<len(s):
            ch=s[r]
            window_count[ch]=window_count.get(ch,0)+1
            if ch in t_count and window_count[ch]==t_count[ch]:
                matches+=1
                while l<=r and matches==requered_count:
                    window_size=(r-l)+1
                    if window_size<ans_len:
                        ans_len=window_size
                        ans_l=l
                        ans_r=r
                    left=s[l]
                    window_count[left]-=1
                    if left in t_count and window_count[left]<t_count[left]:
                        matches-=1
                    l+=1
            r+=1
        return s[ans_l:ans_r+1] if ans_len!=float("inf") else ""       