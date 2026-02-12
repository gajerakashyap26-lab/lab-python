#1.String
#a:Text
import sys

text = sys.argv[1]
print("You entered:", text)

#b:Full Name
import sys

first_name = sys.argv[1]
last_name = sys.argv[2]

print("Full Name:", first_name, last_name)


#2.Int
#a:Addition of Two Integers
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum =", a + b)

 #b:Find Maximum of Two Integers
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Maximum =", max(a, b))


#3.Float
#a:Addition of Two Float Numbers

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

print("Sum =", a + b)


#b:Area of Circle
import sys

radius = float(sys.argv[1])
area = 3.14 * radius * radius

print("Area of circle =", area)


#4.Bool
#a:Check Voting Eligibility (Boolean Condition)

import sys

age = int(sys.argv[1])
is_eligible = age >= 18

print("Eligible for voting:", is_eligible)


#b:Check if Number is Positive
import sys

num = int(sys.argv[1])
print("Is Positive:", num > 0)
