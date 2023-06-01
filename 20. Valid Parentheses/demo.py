class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {")": "(", 
                    "}": "{", 
                    "]": "["}

        start_bracket = []

        for v in s:
            if v in ["(", "{", "["]:
                start_bracket.append(v)

            if v in [")", "}", "]"]:
                if len(start_bracket)==0:
                    return False

                if pair_dict[v] == start_bracket[-1]:
                    start_bracket.pop(-1)
                else:
                    return False

        if len(start_bracket)>0:
            return False
        
        return True


if __name__ == "__main__":
    #s = "()[]{}"
    s = "(]"

    sl = Solution()
    ans = sl.isValid(s)
    print(ans)