class Solution:
    def longestPalindrome_my_first(self, s: str) -> str:
        def check_same(current_list):
            current_n = len(current_list)
            i = 0
            j = current_n -1 -i
            while i < j:
                if current_list[i] != current_list[j]:
                    return False

                i +=1
                j -=1
            return True

        n = len(s)
        l_max = 1
        ans = s[0]
        for i in range(n):
            for j in range(i+l_max, n+1):
                current_list = s[i:j]

                if len(current_list)>l_max:                    
                    if check_same(current_list):
                        l_max = len(current_list)
                        ans = current_list
        return ans

    def longestPalindrome(self, s):
        self.maxlen = 0
        self.start = 0
        
        for i in range(len(s)):
            self.expandFromCenter(s,i,i)
            self.expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxlen]
        

    def expandFromCenter(self,s,l,r):
        while l > -1 and r < len(s) and s[l] ==s[r]:
            l -= 1
            r += 1
        
        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l + 1


if __name__ == "__main__":
    sl = Solution()
    s = "aaaaaaaaaaabcaaaaaaaa"
    ans = sl.longestPalindrome(s)
    print(ans)