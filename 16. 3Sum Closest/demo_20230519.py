from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans:int = None

        for i in range(n):
            l = i+1
            r = n-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]

                if (ans is None) or (abs(ans-target) > abs(s-target)):
                    ans = s

                if target>s:
                    l += 1
                elif target<s:
                    r -= 1
                else:
                    return target
        return ans
                
            
    

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    nums = [0,0,0]
    target = 1

    sl = Solution()
    ans = sl.threeSumClosest(nums, target)

    print(ans)