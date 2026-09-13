number =int(input('Enter N: '))
even_count = 0
odd_count = 0
Even = "Even"
odd = "odd"
for i in range(1, number+1):
    if (i % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
print("Even: ", even_count)
print("odd: ", odd_count)            