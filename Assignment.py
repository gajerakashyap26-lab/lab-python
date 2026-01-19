#1.Write a python program to Display a welcome message.

print("Welcome..!!")

#2.Write a python program to print an address

print("Rajesh Kumar") 
print("Flat No.101, Sunship Apartrment")
print("MG Road Sector 15")
print("Rajkot")
print("Pincode : 360004")
print("India")

#3.Write a program to perform to perform 4 basic mathematical operation(+,-,x,/)using the values 150 and 120.50 

a=150
b=120.50

#a.Addition
print("Addition",a+b)

#b.subtraction
print("Subtraction",a-b)

#c.Multiplication
print("Multiplication",a*b)

#d.Division
print("Division",a/b)

#4.Write a program that calculate the Area of the circle.

radius = float(input("Enter the radius of the circle: "))

area = 3.14159 * radius * radius

print("Area of the circle:", area)

#5.Write a program that calculates the simple interest using formula (PRT)/100

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)


#6.Write a program to calculate the perimeter of a rectangle.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

perimeter = 2 * (length + breadth)

print("Perimeter of the rectangle:", perimeter)


#7.Write a program to calculate the area and perimeter of a rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)


#8.Write a perform that calculate perimeter of a triangle.

a = float(input("Enter side 1 of the triangle: "))
b = float(input("Enter side 2 of the triangle: "))
c = float(input("Enter side 3 of the triangle: "))

perimeter = a + b + c

print("Perimeter of the triangle:", perimeter)


#9.Write a program that calcutates the area and perimeter of a square

side = float(input("Enter the side of the square: "))

area = side * side
perimeter = 4 * side

print("Area of the square:", area)
print("Perimeter of the square:", perimeter)


#10.Write a program that calcutates the perimeter of a square

side = float(input("Enter the side of the square: "))

perimeter = 4 * side

print("Perimeter of the square:", perimeter)