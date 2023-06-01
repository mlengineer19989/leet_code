class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            l = i + 1
            r = n - 1

            if i==0:
                ans = nums[i] + nums[r] + nums[l]
                c_diff = target - ans

            while  l<r:
                cand = nums[i] + nums[r] + nums[l]
                new_diff = target - cand

                if abs(new_diff) < abs(c_diff):
                    ans = cand
                    c_diff = new_diff

                if new_diff == 0:
                    return target
                elif new_diff > 0:
                    l += 1
                elif new_diff < 0:
                    r -= 1
        return ans

if __name__ == "__main__":
    # nums = [-1,2,1,-4]
    # target = 1

    nums = [0,0,0]
    target = 1

    sl = Solution()
    ans = sl.threeSumClosest(nums, target)
    print(ans)