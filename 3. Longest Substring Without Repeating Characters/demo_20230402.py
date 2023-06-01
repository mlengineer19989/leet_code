class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss:str = ""
        current_len:int = 0

        for char in s:
            if char in ss:
                ss = ss[ss.index(char)+1:]
            ss += char
            current_len = max(len(ss), current_len)
        return current_len
            


if __name__ == "__main__":
    s = "abcabcbb"
    #s = "bbbbb"
    #s = "pwwkew"
    #s="b"
    #s = "dvdf"

    sl = Solution()
    ans = sl.lengthOfLongestSubstring(s)

    print(ans)