def palindrome_number(n: int) -> bool:
    """Checks if a number is a palindrome"""
    rev, temp = 0, n
    while temp > 0:
        digit = temp % 10
        rev = (rev * 10) + digit
        temp = temp // 10
       
    return True if n == rev else False

def largest_palindrome_number() ->tuple[int, list]:
    """
    Return the largest palindrome made from the product of two 3-digit numbers.
    """
    pali_list, multiples = [], []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if palindrome_number(i*j):
                multiples.append(f"{i} * {j} = {i*j}")
                pali_list.append(i*j)
    return max(pali_list), multiples

m, p = largest_palindrome_number()
print(f"The largest  largest palindrome made from the product of two 3-digit numbers is {m}.")
for i in p:
    if str(m) in i:
        print(f"The two 3-digit numbers are {i[:3]} and {i[6:9]}.")
        break
