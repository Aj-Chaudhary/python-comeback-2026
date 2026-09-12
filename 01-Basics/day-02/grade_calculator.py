Name = input('Enter Your Name:')
Marks = int(input('Enter Your Marks: '))
if(Marks>=90 and Marks<=100):
    print("A+")
elif(Marks>=80 and Marks<90):
    print("A")
elif(Marks>=70 and Marks<80):
    print("B+")
elif(Marks>=60 and Marks<70):
    print("B")
elif(Marks>=50 and Marks<60):
    print("C")
else:
    print("Fail")                    