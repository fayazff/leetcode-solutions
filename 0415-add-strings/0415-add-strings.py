class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        dummy=[]
        carry=0
        while i>=0 or j>=0 or carry:
            curr_i=int(num1[i]) if i>=0 else 0
            curr_j=int(num2[j]) if j>=0 else 0

            total=curr_i+curr_j+carry
            digit=total%10

            # Convert digit back to string and add to result
            dummy.append(str(digit))

            carry=total//10
            
            i-=1
            j-=1

        # Since we built the number backwards, reverse it
        dummy.reverse()
        return ''.join(dummy)
