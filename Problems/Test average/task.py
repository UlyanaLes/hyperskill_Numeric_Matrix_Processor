def average_mark(*args):
    total = 0
    for el in args:
        total += el
    return round(total / len(args), 1)
