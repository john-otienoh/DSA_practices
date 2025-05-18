def weird_algorithm(n: int):
    """
        Consider an algorithm that takes as input a positive integer n. 
        If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. 
        The algorithm repeats this, until n is one.
    """
    results = [n]
    if n < 0:
        return 'N must be a positive integer'
    while n != 1:
        if n % 2 == 0:
            results.append(n // 2)
            n //= 2
        else:
            results.append((n*3)+1)
            n = (n*3) + 1
    return results

if "__main__" == __name__:
    inp = int(input("Enter a number: "))
    for i in weird_algorithm(inp):
        print(f"{i} ", end="")
    print()