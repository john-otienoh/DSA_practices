def sum_square_difference(n: int) -> tuple[int, int, int]:
    """
    Difference between the sum of the squares of natural numbers 
    and the square of the sum
    """
    sum_of_squares = [i**2 for i in range(0, n+1)]
    square_of_sum = [i for i in range(0, n+1)]
    differences = sum(square_of_sum)**2 - sum(sum_of_squares)
    return differences, sum(square_of_sum)**2, sum(sum_of_squares)

if "__main__" == __name__:
    num = int(input("Enter a Number: "))
    d, sq, sm = sum_square_difference(num)
    print(f"The sum of the squares of the first {num} natural numbers is {sm}")
    print(f"The square of the sum of the first {num} natural numbers is is {sq}")
    print(f"The difference between the sum of the squares of the first {num} natural numbers and the square of the sum is {sq} - {sm} = {d}")
    