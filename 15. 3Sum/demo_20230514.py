from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans:List[List[int]] = []
        L = len(nums)
        nums = sorted(nums)
        
        for i in range(L):
            l = i+1
            r = L-1
            while l<r:
                arr = sorted([nums[i], nums[l], nums[r]])
                val = sum(arr)

                if val>0:
                    r -= 1
                elif val<0:
                    l += 1
                else:
                    if arr not in ans:
                        ans.append(arr)
                    r -= 1
                    l += 1


        return ans

    
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    nums = [0,1,1]
    #nums = [0,0,0]

    sl = Solution()
    ans = sl.threeSum(nums=nums)

    print(ans)