def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    result = []
    for num in a:
        table[num] = num       
        if -num in table and num != 0:     
            result.append(abs(num))

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
