class Solution:
    def letterCombinations_first(self, digits: str) -> list[str]:
        self.digits = digits
        self.n = len(digits)
        self.num2letter_dict = {"2":"abc",
                                "3":"def",
                                "4":"ghi",
                                "5":"jkl",
                                "6":"mno",
                                "7":"pqrs",
                                "8":"tuv",
                                "9":"wxyz"}
        self.ans = []
        if self.n == 0:
            return self.ans

        ind = 0
        let_comb = ""

        self.make_loop(ind, let_comb)
        return self.ans

    def make_loop(self, ind, let_comb):
        if ind <self.n:
            for letter in self.num2letter_dict[self.digits[ind]]:
                self.make_loop(ind+1, let_comb+letter)

        else:
            self.ans.append(let_comb)
            return


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, dic, path + i, res)



if __name__ == "__main__":
    digits = "23"

    sl = Solution()
    ans = sl.letterCombinations_first(digits)
    print(ans)