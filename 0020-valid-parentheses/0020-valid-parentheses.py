class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range (len(s)):
            if s[i]=="(" or s[i]=='{' or s[i]=="[":
                st.append(s[i])
            else:
                if not st:
                    return False
                dumy=st.pop()
                if s[i]==")" and dumy!="(":
                    return False
                elif s[i]=="}" and dumy!="{":
                    return False
                elif s[i]=="]" and dumy!="[":
                    return False
        if len(st)==0:
            return True
        else:
            return False