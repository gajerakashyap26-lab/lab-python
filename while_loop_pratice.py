#while loop

#1.print no. from 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

#2.sum of numbers take user input
n=int(input("enter a number: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("sum is",sum)

#3.print odd no. between 1 to 20
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1


#4.print table of 4
i=1
while i<=10:
    print(4,"x",i,"=",4*i)
    i+=1


#5.print reverse number from 1 to 20
i=20
while i>=1:
    print(i)
    i-=1


#6.find largest no.in the list
numbers=[10,20,5,30,15]
i=0
largest=numbers[0]
while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    i+=1
print("largest number is",largest)

#7.print even no. b/t 1 and 20
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

