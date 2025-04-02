class Solution:
    """Class Palindrome"""
    def palindrome(self, x: int) -> bool:
        """Given an integer x, 
        return true if x is a palindrome, and false otherwise.
        """
        rev, temp = 0, x
        while temp > 0:
            digit = temp % 10
            rev = (rev * 10) + digit
            temp = temp // 10
        return True if x == rev else False

if "__main__" == __name__:
    sol = Solution()
    n = int(input("Enter number to check if its a plindrome: "))
    print(sol.palindrome(n))
