class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        strs.sort()
        first_strs, last_strs = strs[0], strs[-1]
        min_len, i = min(len(first_strs), len(last_strs)), 0
        while i < min_len and first_strs[i] == last_strs[i]:
            i += 1
        return first_strs[:i]

if "__main__" == __name__:
    sol = Solution()
    n = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(sol.longest_common_prefix(n))
