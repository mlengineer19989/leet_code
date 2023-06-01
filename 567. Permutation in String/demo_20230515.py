from typing import Dict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        
        target_dict:Dict[str, int] = {key:s1.count(key) for key in s1}
        for i in range(0,n2 - n1 + 1):
            eval_dict:Dict[str, int] = {key:0 for key in s1}
            eval_str = s2[i:i+n1]
            for key in eval_str:
                if key in eval_dict.keys():
                    eval_dict[key] += 1
            if all([target_dict[key]==eval_dict[key] for key in target_dict.keys()]):
                return True
        return False
            

    

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"

    # s1 = "ab"
    # s2 = "eidboaoo"

    # s1 = "adc"
    # s2 = "dcda"

    # s1 = "hello"
    # s2 = "ooolleoooleh"

    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"

    sl = Solution()
    ans = sl.checkInclusion(s1=s1, s2=s2)

    print(ans)