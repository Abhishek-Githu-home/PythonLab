###Input function
#The input() function is able to read data entered by the user
#And to return the same data to the running program.

print("My name is Abhishek")
role = input()
print("My name is Abhishek and ", role)
#Expected output = My name is Abhishek and  <Provided input>

role = input("He is good at ")
print("And he is doing", role, "Job")
#Expected output = And he is doing <provided input> Job

value = float(input("Enter a number : "))
result = value ** 2.0
print("The square of ", value, "is", result)
#Expected output = The square of  9.0 is 81.0

num1 = int(input("Enter a num01: "))
num2 = int(input("Enter a num02: "))
output = num2 - num1
print("The difference between the two numbers is : ", output)
#Expected output = The difference between the two numbers is :  2

x = float(input("The provided value for first length: "))
y = float(input("The provided value for second length: "))
sum = x ** y + x - (y + x)
print("The sum is" , sum)
#Expected output = The sum is 5.0

#Concatenation operator
fname = input("Can i have your first name please? ")
lname = input("Can i have your second name please? ")
print("The user name is", fname, lname)
print("The user name is " + fname + lname)
#Expected output = The user name is Abhi shek
#Expected output = The user name is Abhishek

#Replication
name = "Jil"
replica1 = name * 3
replica2 = 4 * "Abhi"
print("The replacated name is : ", replica1)
print(replica2)
#Expected output : The replacated name is :  JilJilJil
#Expected output : AbhiAbhiAbhiAbhi

x = int(input("The input of X to determine Y is: "))
y = 1/(x + 1/(x + 1/(x+1/x)))
print("The value of Y is : ", y)
#Expected output : The value of Y is :  0.09901951266867294



