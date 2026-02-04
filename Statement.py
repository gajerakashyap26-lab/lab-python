#1.Vote
age=int(input("Enter your age:"))
if age>=18:
    print("Yes, you are eligible for vote..!!")
else:
    print("No, you are not eligible for vote..!!")

#2.Mark
marks=int(input("Enter your Marks:"))
if marks>=90:
    print("You get A grade.")
elif marks>=70:
    print("You get B grade")
else:
    print("You get C grade")

#3.ODD/EVEN
Number=int(input("Enter the number:"))
if Number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#4.Positive or Negative
Number=int(input("Enter the number:"))
if Number > 0:
    print("The number is positive")
else:
    print("The number is Negative")

#5.Licence Eligible
Num=int(input("Enter the number:"))
if Num >=18:
    print("Yes,you are eligible for Driving licence..!!")
else:
    print("Sorry,you are not eligible for Driving licence..!!")