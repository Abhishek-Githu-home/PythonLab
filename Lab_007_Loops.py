#for Loop: Iterates over a sequence or iterable, executing a block of code for each item.
#while Loop: Repeats a block of code as long as a specified condition is True.
#continue Statement: Skips the current iteration of a loop and moves to the next iteration.
#break Statement: Exits the loop prematurely, ending the loop's execution.
#if-else Statement: Executes a block of code conditionally based on whether a specified condition is True or False.
#Nested Loop: A loop inside another loop, allowing for multi-dimensional iteration through data structures.
#Infinite Loop: A loop that runs indefinitely due to a condition that always evaluates to True, often needing an external break or exit condition.

Count = 100
while Count < 105:
    print(Count)
    Count+= 1

## The Range function (Generates a sequence of numbers for looping.
#Syntax: range(start, stop, step))


for number in range(4):
    print("Attempt", number + 1)
#Prints out the numbers Attempt 1, Attempt 2,Attempt 3,Attempt 4


for i in range(10):
    print("The value of i is : ", i)
#Prints out the numbers The value of i is :  0, The value of i is :  1 , The value of i is :  2, The value of i is :  3, The value of i is :  4, The value of i is :  5, The value of i is :  6, The value of i is :  7, The value of i is :  8, The value of i is :  9

for i in range (2,5):
    print("The value of i is", i)
 #Prints out the numbers The value of i is 2,The value of i is 3,The value of i is 4

for i in range (2,8,4):
    print("The value of i is", i)
#The value of i is 2, The value of i is 6

for i in range (5,2):
    print("The difference of i is", i)
#No output since the range(start, stop, step) and Python expects the start number to be lower than the stop number. It checks: "Is 5 less than 2?" Since the answer is No,
#the loop condition is met immediately, the sequence is treated as empty, and the loop body is never executed.

#The Break Statement (Used to exit the loop prematurely.)
fruits = ["Apple", "Banana", "Orange"]
for x in fruits:
    print(x)
    if x == "Banana":
        break
# Prints out: Apple, Banana

Fruit_Name = ["Banana", "Apple", "Cherry"]
for x in Fruit_Name:
    if x == "Cherry":
        break
    print(x)
# Prints out: Banana, Apple, Cherry

## The Continue statement (Skips the current iteration and continues with the next.)
Names = ["Abhi", "Krishna", "Arjun", "Kunthi", "Preethi"]
for x in Names:
    if x == "Krishna":
        continue
    print(x)
# Prints out: Abhi, Arjun, Kunthi, Preethi

## Else in for loop (Code block executed after the loop completes, but not if exited with break.)
for x in range(6):
        print(x)
else:
    print("Not in range")



for x in range(7,14):
    if x == 9:
        break
    print(x)
else:
    print("Done")
# Prints out: 7, 8

## Nested Loops (A nested loop is a loop inside a loop.)
#The "inner loop" will be executed one time for each iteration of the "outer loop":)

product = ["Fan", "Machine", "Toolkit", "Pen"]
Cost = [100, 200, 300]

for x in product:
    for y in Cost:
        print (x, y)
#Fan 100, Fan 200, Fan 300, Machine 100 ,Machine 200, Machine 300, Toolkit 100, Toolkit 200, Toolkit 300, Pen 100 , Pen 200, Pen 300

## The Pass statement (Used to handle empty loops without causing an error)
for x in [100, 200, 5]:
    pass

#A junior magician has picked a secret number. He has hidden it in a variable named secret_number.
## He wants everyone who runs his program to play the Guess the secret number game, and guess what number he has picked for them.
### Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# 1. Initial ask
number = int(input("Enter an integer number: "))

# 2. Loop WHILE the number is NOT EQUAL to secret_number
while number != secret_number:
    # Everything indented here happens if they get it WRONG
    print("Ha ha! You're stuck in my loop!")
    
    # 3. Ask again (Update the 'number' variable)
    number = int(input("what is the secret number? "))

# 4. This runs only when the loop finishes (when they get it right)
print("Well done, muggle! You are free now.")
