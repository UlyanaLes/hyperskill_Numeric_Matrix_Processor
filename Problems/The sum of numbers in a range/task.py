def range_sum(numbers_arg, a_arg, b_arg):
    sum_el = 0
    for el in numbers_arg:
        if a_arg <= el <= b_arg:
            sum_el += el
    return sum_el


numbers = list(map(int, input().strip().split()))
a, b = map(int, input().strip().split())
print(range_sum(numbers, a, b))
# print(numbers)
# print(a, b, sep='\n')
