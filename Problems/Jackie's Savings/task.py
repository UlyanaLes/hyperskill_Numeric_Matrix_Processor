def final_deposit_amount(*interest, amount=1000):
    for el in interest:
        amount = amount * (1 + el / 100)
    return round(amount, 2)


percent = (5, 7, 4)
print(final_deposit_amount(*percent, 2000))
