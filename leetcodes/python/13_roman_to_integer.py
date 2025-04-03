class Solution:
    def roman_to_int(self, s: str) -> int:
        if not s:
            return -1
        roman_integer = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        i = 0
        while (i < len(s)):
            s1 = roman_integer[s[i]]
            if (i+1 < len(s)):
                s2 = roman_integer[s[i+1]]
                if (s1 >= s2):
                    total += s1
                    i += 1
                else:
                    total -= s1
                    i += 1
            else:
                total +=  s1
                i += 1
        return total

if "__main__" == __name__:
    sol = Solution()
    n = input("Enter roman numeral: ")
    print(sol.roman_to_int(n))

# translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]