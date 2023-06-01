class Solution:
    def __init__(self) -> None:
        self.current_state = 0
        self.s_sign = 1
        self.s_int = 0

    def myAtoi(self, s: str) -> int:
        self.n = len(s)
        if self.n == 0:
            return 0

        for v in s:
            if v.isdigit():
                self.s_int =10*self.s_int + int(v)
                self.current_state = 2

            elif (v == "+" or v=="-") and self.current_state == 0:
                if v == "-":
                    self.s_sign = -1
                self.current_state = 1

            elif v == " " and self.current_state == 0:
                self.current_state = 0

            else:
                break
            
        ans = self.s_sign*self.s_int
        ans = self.validate(ans)
        return ans

        

    def validate(self, s):
        ans = max(s, -2**31)
        ans = min(ans, 2**31 - 1)
        return ans

if __name__ == "__main__":
    s = "   -42"
    #s = "4193 with words"
    #s = "words and 987"
    sl = Solution()
    ans = sl.myAtoi(s)
    print(ans)
