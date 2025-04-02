class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_index_map = {}
        for i, j in enumerate(nums):
            value = target - j
            if value in num_index_map:
                return [num_index_map[value], i]
            num_index_map[j] = i
        return []

if "__main__" == __name__:
    sol = Solution()
    n, t = [7, 2, 13, 11], 15
    print(sol.twoSum(n, t))
    