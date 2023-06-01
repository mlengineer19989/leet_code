from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        target_s = strs[0]

        for i, c in enumerate(target_s):
            try:
                for s in strs[1:]:
                    if c == s[i]:
                        continue
                    else:
                        return ans
                ans += c
            except:
                return ans
        return ans
    
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    #strs = ["dog","racecar","car"]
    strs = ["flower","flow","flo"]

    sl = Solution()
    ans = sl.longestCommonPrefix(strs)
    print(ans)        