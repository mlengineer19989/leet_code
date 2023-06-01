class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str_set = list(set(ransomNote))

        for i in str_set:
            if ransomNote.count(i) <= magazine.count(i):
                ans = True 
            else:
                ans = False
                break

        return ans



if __name__ == "__main__":
    demo = Solution()
    ans = demo.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")
    print(ans)