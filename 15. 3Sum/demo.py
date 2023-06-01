class Solution:
    def threeSum_first(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            num_i = nums[i]
            if num_i > 0:
                return ans

            else:
                for j in range(i+1, n):
                    num_j = nums[j]
                    for k in range(j+1, n)[::-1]:
                        num_k = nums[k]
                        if num_i+num_j+num_k==0:
                            cand = sorted([num_i, num_j, num_k])
                            if cand not in ans:
                                ans.append(cand)
                            break

        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)


if __name__ == "__main__":
    #nums = [-1,0,1,2,-1,-4]
    #nums = [0,1,1]
    nums = [0,0,0]

    sl = Solution()
    ans = sl.threeSum(nums)
    print(ans)