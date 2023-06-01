class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {"I" : 1,
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000}
        
        ans = 0
        for c_current, c_next in zip(s, s[1:]):
            sign = -1 if num_dict[c_current] < num_dict[c_next] else 1
            ans += sign*num_dict[c_current]

        ans += num_dict[s[-1]]
        return ans
    
if __name__ == "__main__":
    s = "III"
    s = "LVIII"
    s = "MCMXCIV"

    sl = Solution()
    ans = sl.romanToInt(s)

    print(ans)
    
