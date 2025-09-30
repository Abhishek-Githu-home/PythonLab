#####Variables#####
#A variable comes into existence as a result of assigning a value to it. Storing a value into it.
var = 123
print(var)
#Expected output = 123

char = 24
name = 'Abhishek'
section = 'A'
Roll_ID = 8349022
GAME = 'Chess'
print(char, name, section, Roll_ID, GAME)
#Expected output = 24 Abhishek A 8349022 Chess

print("His name is " + name  + " and intersting in playing " + GAME)
#Expected output = His name is Abhishek and intersting in playing Chess

#Assigning value to existing variable
value = 123
print(value)
value = value + 123
print(value)
#Expected output = 246

x = 45
x = x + 1
print(" The value is " , x )
#Expected output = The value is  46


a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 2
print("c =", c)
#Expected output : c = 625.0

John = 3
Mary = 5
Adam = 6
total_apples = John + Mary + Adam
Cost_of_apples = John * 30 + Mary * 30 + Adam * 30
print(John, Mary, Adam, sep=",")
print(total_apples)
print(Cost_of_apples)
#Expected output = 3,5,6
                    # 14
                    # 420

##Shortcut operators
m = 2
m *= 3 # m = m * 3
sheep = 99
sheep += 1 #sheep = sheep + 1
rem = 9
rem%= 4 #rem = rem % 4
print(sheep, m, rem, sep=",")
#Expected output = 100,6,1

##Sample Problem
kilometers = 10
miles = 5

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print("The Kilometers of", kilometers , " is ", kilometers_to_miles , "miles")
print("The Miles of", miles , " is " , miles_to_kilometers , "kilometers")

#Expected output =#The Kilometers of 10  is  6.211180124223602 miles
                  #The Miles of 5  is  8.05 kilometers


##Reserved Keywords : ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

