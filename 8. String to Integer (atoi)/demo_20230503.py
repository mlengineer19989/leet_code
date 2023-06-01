import typing as tp

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        
        if len(s)==1 and s.isdecimal():
            return int(s)

        ans:int = 0
        sign:int = 1

        for i, (cv, nv) in enumerate(zip(s, s[1:])):

            if cv.isdecimal():
                ans = 10*ans + int(cv)
                if nv.isdecimal() == False:
                    break
            else:
                if self.issign(cv) and nv.isdecimal():
                    sign = int(cv + "1")
                elif (cv == " "):
                    continue
                else:
                    break

            if (i == len(s)-2) and (cv.isdecimal() or self.issign(cv)) and nv.isdecimal():
                ans = 10*ans + int(nv)

        return max(min(sign*ans, 2**31 -1), -2**31)
    
    def issign(self, c:str) -> bool:
        if (c == "+") or (c == "-"):
            return True
        else:
            return False
    

if __name__ == "__main__":
    s = "4193 with words"
    #s = "words and 987"
    #s = "42"
    #s = "   -42"
    #s = ".1"
    #s = ""
    #s = "1"
    #s = "s1s"
    s = "+1"

    sl = Solution()
    ans = sl.myAtoi(s=s)
    print(ans)