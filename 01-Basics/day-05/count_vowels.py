word = input("Enter a word: ")
vowels = "aeiou"
count = 0

for char in word:
    if char.lower() in vowels:
        count = count + 1

print(f"Vowel count: {count}")