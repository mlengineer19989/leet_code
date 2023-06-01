from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        l = 0
        r = len(height)-1
        ans = 0

        while l<r:
            ans = max(ans, self.calc_area(l, r, height))
            if height[l] < height[r]:
                l += 1
            else:
                r -=1

        return ans

    def calc_area(self, l, r, height):
        return (r - l) * min(height[l], height[r])
    

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height = [1, 2, 1, 2]
    height = [1,2,4,3]

    sl = Solution()
    ans = sl.maxArea(height)

    print(ans)