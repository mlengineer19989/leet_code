class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0

        state:str = "s0"
        ans:int = 0
        sign:int = 1

        for v in s:
            if state == "s0":
                if v == " ":
                    state = "s0"
                elif (v == "+") or (v == "-"):
                    state = "s1"
                    sign = 1 if v == "+" else -1
                elif v.isdigit():
                    state = "s2"
                    ans = 10*ans + int(v) 
                else:
                    return 0
                
            elif state == "s1":
                if v.isdigit():
                    state = "s2"
                    ans = 10*ans + int(v)
                else:
                    return 0
                
            elif state == "s2":
                if v.isdigit():
                    state = "s2"
                    ans = 10*ans + int(v)
                else:
                    break

        return max(min(sign * ans, 2**31-1), -2**31)
                
if __name__ == "__main__":
    s = "42"
    s = "   -42"
    s = "4193 with words"

    sl = Solution()
    ans = sl.myAtoi(s=s)

    print(ans)