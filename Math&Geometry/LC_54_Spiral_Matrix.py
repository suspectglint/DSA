class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Here we are initializing top and left to zero.
        #And bottom to (number of rows + 1) and right to (number of columns + 1)
        #+1 for better looping purpose.

        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])

        result = []

        #Breaking condition - top<bottom and left<right - if this is false
        #then we stop the solution.

        while top<bottom and left<right:

            # Add the elements on the top side from left to right
            for i in range(left,right):
                result.append(matrix[top][i])

            #Increase top by 1
            top+=1

            # Add the elements on the right side from top to bottom
            for i in range(top,bottom):
                result.append(matrix[i][right-1])

            #Decrese right by 1
            right-=1

            #Here we check whether condition fails or not because for singular row or
            #singular column matrices the condition fails after one iteration itself.
            if not (top<bottom and left<right):
                break

            # Add the elements on the bottom side from right to left
            #print(right-1,left-1)
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])

            #Decrease bottom by 1
            bottom-=1

            # Add the elements on the left side from bottom to top
            #print(bottom-1,top-1)
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])

            #Increase left by 1
            left+=1

        return result