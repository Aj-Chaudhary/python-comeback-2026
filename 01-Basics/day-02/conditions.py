Name = input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))
if(Age < 18):
    print("Minor")
elif (Age >= 18 and Age < 60):
    print("Adult")
else:
    print("Senior Citizen")     