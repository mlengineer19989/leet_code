

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_max = 0
        cw = ""
        if len(s)>0:
            for w in s:
                if w in cw:
                    i_same = cw.index(w)
                    cw = cw[i_same+1:]
                
                cw += w
                l_max = len(cw) if len(cw) > l_max else l_max

        return l_max

if __name__=="__main__":
    sl = Solution()
    s = "abcabcbb"
    ans = sl.lengthOfLongestSubstring(s)
    print(ans)