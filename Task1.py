#1.Find maximum of 2 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Maximum number is:", a)
else:
    print("Maximum number is:", b)

    
#2.Find the length of string

text = input("Enter a string: ")

length = len(text)

print("Length of the string:", length)


#3.Find number 1 to 5

for i in range(1, 6):
    print(i)


#4.Calculate simple intrest

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)


#5.Print welcome message

print("Welcome..!!")


#6.print First character of a string

text = input("Enter a string: ")

print("First character:", text[0])


#7.print last character of a string

text = input("Enter a string: ")

print("Last character:", text[-1])


#8.Check positive or negative number

a = float(input("Enter the number : "))

if a > 0 :
        print("The given number is positive..!!")
elif a < 0 :
        print("The given number is negative..!!")  
else :
        print("The given number is zero..!!")


#9.Add 3 numbers

a = float(input("Enter the first number : "))
b = float(input("Enetr the second number : "))
c = float(input("Enter the third number : "))

print("The addition of a,b and c is : ",a+b+c)


#10.Take a input from the user and make a task

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

