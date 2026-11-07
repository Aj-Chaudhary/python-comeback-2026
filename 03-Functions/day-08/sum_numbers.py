def sum_all(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print(sum_all(1, 2, 3))
print(sum_all(5, 10))
print(sum_all())