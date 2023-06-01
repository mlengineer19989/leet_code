class Solution:
    def reverse(self, x: int) -> int:
        x_sign = self.sign(x)
        x_abs = abs(x)

        x_abs_str = str(x_abs)
        ans = int(x_abs_str[::-1])
        ans = self.validate(ans)
        return x_sign * ans

    def sign(self, x):
        if x<0:
            ans = -1
        else:
            ans = 1
        return ans

    def validate(self, x: int):
        if x< -2**31 or 2**31-1 < x:
            ans = 0
        else:
            ans = x
        return ans

if __name__ == "__main__":
    x = -12300000000000
    sl = Solution()
    ans = sl.reverse(x)
    print(ans)