"""class Solution:
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            newSubsets = []
            for curr in output:
                temp = curr.copy()
                temp.append(num)
                newSubsets.append(temp)
            for curr in newSubsets:
                output.append(curr)
            print(curr,newSubsets)
        return output
    
sol = Solution()    
print(sol.subsets([1,2,3]))"""

class Solution:
    def subsets(self, nums):
        self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        # Add the current subset to the output
        self.output.append(curr[:])
        print(curr,self.output,id(curr))
        # Generate subsets starting from the current index
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()

sol = Solution()    
print(sol.subsets([1,2,3]))