class Solution:
    def reverse(self, x: int) -> int:
        q = abs(x)
        ans = 0
        mod = 0
        while q != 0:
            mod = q%10
            q = q//10
            ans = 10*ans + mod
        return self.eval(self.sign(x)*ans)
    
    def sign(self, x:int) -> int:
        return 1 if x>=0 else -1
    
    def eval(self, x:int) -> int:
        if (-2**31 < x) and (x < 2**31 - 1):
            return x
        else:
            return 0
    

if __name__ == "__main__":
    x = 123
    #x = -123
    #x = 120
    x = 1534236469

    sl = Solution()
    ans = sl.reverse(x)

    print(ans)