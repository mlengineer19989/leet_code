from typing import List, Set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans:Set[List[int]] = set([])
        n = len(nums)
        nums = sorted(nums)

        for i in range(n):
            l = i+1
            r = n-1
            while l<r:
                target = nums[i]+nums[l]+nums[r]
                if (target > 0):
                    r -= 1
                elif (target < 0):
                    l += 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1

        return list(ans)

    

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]

    sl = Solution()
    ans = sl.threeSum(nums)
    print(ans)