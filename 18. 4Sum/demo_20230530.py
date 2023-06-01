from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums = sorted(nums)
        N = len(nums)
        ans:List[List[int]] = []

        for i in range(N-3):
            for j in range(i+1, N-2):
                l = j+1
                r = N-1

                while l < r:
                    arr = [nums[i], nums[j], nums[l], nums[r]]
                    s = sum(arr)

                    if (s == target) and (arr not in ans):
                        ans.append(arr)
                    elif (s < target):
                        l += 1
                    else:
                        r -= 1

        return ans
    

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0

    nums = [2,2,2,2,2]
    target = 8

    sl = Solution()
    ans = sl.fourSum(nums=nums, target=target)

    print(ans)