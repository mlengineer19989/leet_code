class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    break
            else:
                continue

            break

        return ans

if __name__ == "__main__":
    cl = Solution()
    nums = [2,7,11,15]
    target = 9
    print(cl.twoSum(nums, target))

