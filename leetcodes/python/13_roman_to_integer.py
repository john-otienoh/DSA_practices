class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_integer = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        value = 0
        for i in s:
            if i in roman_integer.keys():
                value += roman_integer[i]

        return value

if "__main__" == __name__:
    sol = Solution()
    n = input("Enter roman numeral: ")
    print(sol.roman_to_int(n))
