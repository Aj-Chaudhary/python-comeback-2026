word = input("Enter a word: ")
a = word[::-1]
b = word[:]
if(b == a):
    print("Palindrme!")
else:
    print("Not A Palindrme!")    