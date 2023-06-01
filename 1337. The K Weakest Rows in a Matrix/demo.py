
class Solution:
    def kWeakestRows_first_answer(self, mat: list[list[int]], k: int) -> list[int]:
        "my first answer"
        sol_num_list = [sum(l) for l in mat]
        ans =  [i[0] for i in sorted(enumerate(sol_num_list), key=lambda x:x[1])][:k]
        return ans

    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        "my second answer"
        ans =  [i[0] for i in sorted(enumerate(mat), key=lambda x:sum(x[1]))][:k]
        return ans


if __name__ == "__main__":
    cl = Solution()
    mat = [[1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]]
    k = 3
    ans = cl.kWeakestRows(mat, k)
    print(ans)