class Solution:
    #Approach-1  : Recursive Solution
    #In this approach, we split the n into two parts and calculate pow(x,n//2).
    #If n is even, we calculate pow(x,n//2)**2 and return it
    #else if n is odd, we calculate pow(x,n//2)**2, multiply with x and return it.
    #Total of O(logn) calls are made recursively.
    """def recur(self,x,n):
        if n==1:
            return x
        a = self.recur(x,n//2)
        return a*a if n%2==0 else a*a*x


    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        return self.recur(x,n) if n>0 else 1/(self.recur(x,-n))
    """
    #Approach-2 : Iterative solution - Binary Exponentiation Algorithm
    #In this approach, we use the simple concept x^n = (x^2)^(n/2) if n is even
    #else x^n = x*(x^2)^((n-1)/2).
    #In this iterative approach, since we decrease n to half everytime we use that
    #as a loop conditional.
    #The key in this approach is every n(power) reaches 1 when we right shift by 1 eventually.
    #So we store the final value into res as n=1 is odd and in between whenever the n is odd,
    #we multiply res with x. So finally we end up with correct value.
    def myPow(self, x: float, n: int) -> float:
        power = n if n>0 else -n
        res=1
        while power>=1:
            if x==0:
                return 0
            if power & 1:
                res*=x
            power>>=1
            if power==0:
                break
            x=x*x
        print(res,x)
        return res if n>0 else 1/res