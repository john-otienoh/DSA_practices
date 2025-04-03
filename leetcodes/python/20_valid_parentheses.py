class Solution:
    def is_valid(self, s: str) -> bool:
        stk = []
        d = {'()', '[]', '{}'}
        for i in s:
            if i in '({[':
                stk.append(i)
            elif not stk or stk.pop() + i not in d:
                return False
        return not stk

if "__main__" == __name__:
    sol = Solution()
    n = "()[]{}"
    print(sol.is_valid(n))
