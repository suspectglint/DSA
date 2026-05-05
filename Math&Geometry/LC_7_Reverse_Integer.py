class Solution:
    def reverse(self, x: int) -> int:
        #Approach - FYI, this doesnot involve bit manipulation.
        #As per the problem, we are not allowed to store 64 bit signed or 
        #unsigned integers. And we know the input is a 32-bit signed integer
        #within the range of [-2^31,2^31 - 1]. So we proceed to calculate the
        #reverse of number by taking least significant digit and adding it up
        #to the result.So we calculate last significant digit and divide x/10.
        #But we add it up to res only before we check whether the result
        #may exceed 32 bit size number. 
        #However we need to make sure once we reach the last
        #digit, we have to check whether the result is less than MIN/10 or
        #result == MIN/10 and digit>8. Similarly for MAX, result is greater than
        #MAX/10 or result==MAX/10 and digit>7, then we return 0. 
        MAX = 2147483647
        MIN = -2147483648
        res=0
        while x!=0:
            #print("Before = ",x,res)
            d = int(math.fmod(x,10))
            x=int(x/10)
            #print("Mid = ",x,d)
            if res<int(MIN/10) or ( res==int(MIN/10) and d>8 ):
                return 0
            if res>int(MAX/10) or ( res==int(MAX/10) and d>7 ):
                return 0
            res = res*10 + d
            #print("After = ",x,res)
        return res
