name = input('Enter your name:')
print('Hello!,', name)

#Input + Numbers

age = input('Enter yourr age:')
print('Your age is :', age)

#Here is the imp part
#Input() gives us Str.
#age = input('Enter yourr age:')
#print('Your age is :', age)
#So, this doesnot gives us an integer
#we can convert it as :

age = int(input('Enter yourr age:'))
print('Next year You will be :', age+1)