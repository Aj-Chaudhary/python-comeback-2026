secret = 7

while True:
    guess = int(input('Enter Your guess: '))   
    if guess == secret:
        print("correct guess")
        break                                   
    elif guess > secret:
        print("Too High!")                      
    else:
        print("Too Low!") 