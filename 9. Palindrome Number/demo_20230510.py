class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)

        l = 0
        r = len(str_x)-1
        ans = True

        while l <= r:
            if str_x[l] == str_x[r]:
                l += 1
                r -= 1
            else:
                ans = False
                break
        return ans
    
if __name__ == "__main__":
    x = 121
    x = -121
    x = 10
    x = 1001

    sl = Solution()
    ans = sl.isPalindrome(x=x)

    print(ans)