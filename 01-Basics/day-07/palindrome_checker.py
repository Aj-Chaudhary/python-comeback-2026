def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a Palindrome!")
else:
    print(f"{word} is Not a Palindrome.")