def multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number}*{i}={result}")

n = int(input("Enter a number: "))
multiplication_table(n)