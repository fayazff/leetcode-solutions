class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right=0,len(matrix[0])-1
        top,bottom=0,len(matrix)-1
        mat=[]
        while left<=right and top<=bottom:
            #top row
            for i in range(left,right+1):
                mat.append(matrix[top][i])
            top+=1
            #right colum
            for i in range(top,bottom+1):
                mat.append(matrix[i][right])
            right-=1
            #bottom row
            if top<=bottom:
                for i in range(right,left-1,-1):
                    mat.append(matrix[bottom][i])
                bottom-=1
            #left colum
            if left<=right:
                for i in range(bottom,top-1,-1):
                    mat.append(matrix[i][left])
                left+=1
        return mat

        