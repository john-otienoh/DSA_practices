def repetitions(string: str) -> int:
    """
    You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
    Your task is to find the longest repetition in the sequence.
    This is a maximum-length substring containing only one type of character.
    Input:
        The only input line contains a string of n characters.
    Output
        Print one integer: the length of the longest repetition.
    """
    max_substring_len, count, n = 1, 1, len(string)
    for i in range(1, n):
        if string[i] == string[i-1]:
            count += 1
            max_substring_len = max(max_substring_len, count)
        else:
            count = 1
    return max_substring_len

if "__main__" == __name__:
    inp = input()
    print(repetitions(inp))
