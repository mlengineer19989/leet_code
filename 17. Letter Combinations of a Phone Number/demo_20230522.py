from typing import List, Dict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        self.digits = digits[::-1]
        self.d2l_dict:Dict[int, str] = {2:"abc",
                                        3:"def",
                                        4:"ghi",
                                        5:"jkl",
                                        6:"mno",
                                        7:"pqrs",
                                        8:"tuv",
                                        9:"wxyz"}
        
        return self.backtracking(len(self.digits)-1)
        
    def backtracking(self, i:int) -> List[str]:
        if i==0:
            return [c for c in self.d2l_dict[int(self.digits[i])]]

        ans = []
        for c in self.d2l_dict[int(self.digits[i])]:
            ans += [c+c_d for c_d in self.backtracking(i-1)]

        return ans

if __name__ == "__main__":
    digits = "23"

    sl = Solution()
    ans = sl.letterCombinations(digits)

    print(ans)