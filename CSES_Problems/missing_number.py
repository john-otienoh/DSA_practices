def missing_number(n: int, l: list):
    """
    You are given all numbers between 1,2, ...,n except one.
    Your task is to find the missing number.
    Input:
        The first input line contains an integer n.
        The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
    Output:
        Print the missing number
    """
    return (n * (n + 1) // 2) - sum(l)

if "__main__" == __name__:
    inp, string = int(input("Enter a number: ")), input("Enter a string: ")
    seq = [int(i) for i in  string.split(" ")]
    print(f"The missing number is {missing_number(inp, seq)}")
