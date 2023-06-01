import typing as tp

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0 or len(s)==1:
            return s
        
        max_len:int = 0
        r_max:int = 0
        l_max:int = 0
        
        for l in range(len(s)):
            r:int = self.exapndPalindrome(r=l, l=l, s=s)

            if len(s[l:r])>max_len:
                r_max = r
                l_max = l
                max_len = len(s[l:r])

        return s[l_max:r_max]
    
    def exapndPalindrome(self, r:int, l:int, s:str) -> int:
        for c in range(l, len(s)): 
            if s[l:c]==s[l:c][::-1]:
                r = c
        return r

if __name__ == "__main__":
    s = "babad"
    s = "cbbd"
    s = "a"
    s = "bb"
    # s = ""

    sl = Solution()
    ans = sl.longestPalindrome(s=s)

    print(ans)