from typing import List, Dict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans:List[str] = []
        
        if len(digits)==0:
            return ans

        d2l_dict:Dict[int, str] = {2:"abc",
                                    3:"def",
                                    4:"ghi",
                                    5:"jkl",
                                    6:"mno",
                                    7:"pqrs",
                                    8:"tuv",
                                    9:"wxyz"}
        
        for i, num in enumerate(digits[::-1]):
            if i==0:
                ans += [c for c in d2l_dict[int(num)]]
            else:
                D = []
                for c in d2l_dict[int(num)]:
                    D += [c+c_pre for c_pre in ans]
                ans = D.copy()

        return ans


if __name__ == "__main__":
    digits = "79"

    sl = Solution()
    ans = sl.letterCombinations(digits=digits)

    print(ans)