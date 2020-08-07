def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    for array in arrays:
        for item in array:
            if item not in table:
                table[item] = 1
            else:
                table[item] += 1
    intersections = []
    for item in table:
        if table[item] == len(arrays):
            intersections.append(item)

    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
