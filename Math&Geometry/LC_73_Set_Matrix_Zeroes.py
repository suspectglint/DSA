class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Approach-1 
        #We will create row flags and column flags to store the boolean
        #value which tells whether that row or column has a zero in it.
        #This is calculated in first iteration and in the next iteration
        #we check flags, if either row or column flag is zero, we set the matrix value to zero.
        """
        m=len(matrix)
        n=len(matrix[0])
        rowzeroflag=[False]*m
        colzeroflag=[False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rowzeroflag[i]=True
                    colzeroflag[j]=True
        for i in range(m):
            for j in range(n):
                if rowzeroflag[i] or colzeroflag[j]:
                    matrix[i][j]=0
        """
        #Approach-2
        #In approach-1, we are using additional O(m+n) space to store row and column zero flags.
        #Instead the optimal way is to use first row and first column as flags.
        #First row signifies which column values are supposed to set to be zero.
        #First column signifies which rows values are supposed to set to be zero.
        #And matrix[0][0] cannot mark both values so we use a separate value to track if zerorow is True.
        #Finally, we also need to make sure if matrix[0][0] is True, first column needs to be set to 0.
        #And if zerorow is True, entire first row needs to be set to zero.
        #In the first iteration, we mark flags in first row, first column and zerorow.
        #In the second iteration, we have to traverse only inner rows and columns - IMPORTANT
        #Then we check whether the first column needs to be set to zero by checking matrix[0][0]
        #And then we check first row needs to be set to zero based on rowzero.
        #Space Complexity is O(1) and Time Complexity is O(m*n)
        m=len(matrix)
        n=len(matrix[0])
        rowzero=False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i==0:
                        rowzero=True
                    else:
                        matrix[i][0]=0
                        matrix[0][j]=0
        #print(matrix)               
        for i in range(1,m):
            for j in range(1,n):
                print(i,j,matrix[i][0],matrix[0][j])
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        #print(matrix)
        if matrix[0][0]==0:
            for i in range(m):
                matrix[i][0]=0        
        if rowzero:
            for j in range(n):
                matrix[0][j]=0
