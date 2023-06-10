from typing import Dict

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict:Dict[str, str] = {"(":")",
                                       "[":"]",
                                       "{":"}"}
        target_str:str = ""

        for c in s:
            if c in bracket_dict.keys():
                target_str += bracket_dict[c]
            elif c in bracket_dict.values():
                if (len(target_str)==0) or (c != target_str[-1]):
                    return False
                else:
                    target_str = target_str[:-1]

        if len(target_str)==0:
            return True
        else:
            return False
    

if __name__ == "__main__":
    s = "()[]{}"
    s = "()"
    s = "{[()]}([]}"
    s = ""

    sl = Solution()
    print(sl.isValid(s))