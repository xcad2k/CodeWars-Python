def sort_array(source_array):
    odd = []
    output = []

    # Return a sorted array.
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            odd.append(source_array[i])

    odd.sort(reverse=True)

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            output.append(odd.pop())
        else:
            output.append(source_array[i])

    return output
    
print(sort_array([5, 3, 2, 8, 1, 4]))
