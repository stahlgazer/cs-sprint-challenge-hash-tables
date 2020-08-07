def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    for i in range(length):
        table[weights[i]] = i
        # print(weights[i])
    for i in range(length):
        ## limit 21 - 4, 6, 10, 15, 16, = 17, 15, 11, 6, 5
        a = limit-weights[i]
        print(a)
        if a in table:
            return (max(i, table[a]), min(i, table[a]))

    return None

##                                            0  1  2   3   4
print(get_indices_of_item_weights(weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21))