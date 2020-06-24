def last_indexof_max(numbers):
    # write the modified algorithm here
    max_index = 0
    # max_el=numbers[max_index]
    for i in range(1, len(numbers)):
        if numbers[max_index] <= numbers[i]:
            max_index = i
    return max_index