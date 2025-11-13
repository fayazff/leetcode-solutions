class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        dummy=[0]*(len(num1)+len(num2))
            
        num1,num2=num1[::-1],num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit=int(num1[i])*int(num2[j])
                dummy[i+j]+=digit
                dummy[i+j+1]+=dummy[i+j]//10
                dummy[i+j]=dummy[i+j]%10
        dummy,beg=dummy[::-1],0
        while beg<len(dummy) and dummy[beg]==0:
            beg+=1
        dummy=map(str,dummy[beg:])
        return ''.join(dummy)
        