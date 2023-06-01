class Solution:
    def maxArea_my_first(self, height: list[int]) -> int:
        """my first solution

        Args:
            height (list[int]): _description_

        Returns:
            int: _description_
        """
        n = len(height)

        left = 0
        right = len(height)-1
        H = min(height[left], height[right])
        W = right - left
        area = H * W

        for i in range(n):
            if height[i] >= height[left]:
                for j in range(i+1, n)[::-1]:
                    if height[j] >= height[right]:
                        H = min(height[i], height[j])
                        W = j - i
                        sub = H * W
                        if  sub > area:
                            area = sub
                            left = i
                            right = j
        return area


    def maxArea_my_second(self, height: list[int]) -> int:
        n = len(height)
        area = 0

        for i in range(n):
            for j in range(i+1, n)[::-1]:
                H = min(height[i], height[j])
                W = j - i
                area = max(area, H * W)
        return area

    def maxArea_my_third(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        area = 0

        while left < right:
            area = max(area, min(height[left], height[right])*(right - left))

            if height[left]>=height[right]:
                right -= 1
            else:
                left += 1
        return area

    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea




if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]

    sl = Solution()
    ans = sl.maxArea_my_third(height)
    print(ans)