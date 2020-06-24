def sq_sum(*args):
    total = 0
    for el in args:
        total += el ** 2
    return float(total)

# print(sq_sum(1, 2, 2, 4))  # 25.0
# print(sq_sum(1.5))         # 2.25
# print(sq_sum(1, 10, 10))   # 201.0
