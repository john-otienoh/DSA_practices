""""
If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23

Find the sum of all the multiples of 3 or 5 below 1000
"""
def sum_of_multiples(n: int) -> tuple[int, list]:
    "Returns tuple of (list and sum) of the multiples of a given integer"
    total_sum = 0
    multiples = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
            multiples.append(i)
    return total_sum, multiples

if '__main__' == __name__:
    num = int(input("Enter Number: "))
    s, m = sum_of_multiples(num)
    print(f"The list of all the multiples of 3 or 5 below {num} is {m}.")
    print(f"The sum of all the multiples of 3 or 5 below {num} is {s}.")
