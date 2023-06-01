class Solution:
    def longestCommonPrefix_first(self, strs: list[str]) -> str:
        """my first solution

        Args:
            strs (list[str]): _description_

        Returns:
            str: _description_
        """
        ans = ""
        n_min = min([len(word) for word in strs])

        for i in range(n_min):
            if all(word[i] == strs[0][i] for word in strs):
                ans += strs[0][i]
            else:
                return ans

        return ans

if __name__ == "__main__":
    strs = ["flower","flow","flight"]

    sl = Solution()
    ans = sl.longestCommonPrefix(strs)
    print(ans)