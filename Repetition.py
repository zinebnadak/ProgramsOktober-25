# Python practice set — focusing on:
# Variables & Data types
# Logical conditions (if, elif, else)
# Loops (for, while)
# Functions
# Sets and dictionaries (mappings)
# Classes and objects

# No string manipulation, list/tuple exercises, or error handling included here!





#1. Variables and Data Types
#Goal: Practice assigning, reading, and using variables of different data types.

#1. Create three variables: one integer, one float, and one boolean. Print them all on one line.

integer = 3
name = ("zineb")
is_hungry = True
is_at_the_gym = False

print(integer,name,is_hungry,is_at_the_gym)

#2 Assign the result of 5 * 3 + 2 to a variable result and print it.
result = 5*3+2
print(result)

#3 What happens if you divide an integer by another integer in Python 3?
# Try 7 / 2 and 7 // 2

print(7/2)         #gives you exact result as a decimal, meaning it always returns a float (even if the numbers are integers).
print(7//2)        #performs floor division, meaning it divides the numbers and rounds down to the nearest whole number (integer).
print(7%2)         #oposite of floow devivion,  gives the remainder of a division

#4 Create a variable temperature = 23.7. Convert it to an integer and print the result.
temperature = 23.7
print(int(23.7))

#5 Create two variables, a = 10 and b = "5". Try to add them together. Then fix the error.

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
a=10
b=5
print(a+b)




#2. Logical Conditions (if / elif / else)
#Goal: Understand conditionals and comparison operators.

#6 Ask the user for an integer and print whether it’s positive, negative, or zero.

integer = int(input("Enter an integer:"))

if integer > 0:
    print("The integer is positive!")
elif integer < 0:
    print("The integer is negative!")
else:
    print("The integer you entered is Zero!")

#7 Ask for a number and print “Even” if it’s divisible by 2, otherwise print “Odd.”
print()
number = float(input("Enter a number to check if odd/even!:" ))      #float takes both integers and floats

if number % 2 == 0:
    print(f"Number {number} is even!")
else:
    print(f"Number {number} is odd!")

#8 Create a variable x = 15. Check if x is between 10 and 20 (inclusive).
print()

x = 5

is_between = (10<= x <=20)      #boolean variable

if is_between:
    print (f"Number {x} is between 10 and 20 (inclusive)")
else:
    print (f"Number {x} is NOT between 10 and 20 (inclusive)")

#9 Write an if-elif-else block that checks a variable grade:
#≥ 90 → “A”
#≥ 80 → “B”
# ≥ 70 → “C”
# < 70 → “Fail”

grade = int(input("Enter students grade (max=100):"))

if grade >= 90:
    print("Student got a A!")

elif grade >= 80:
    print("Student got a B!")

elif grade >= 70:
    print("Student got a C!")

elif grade < 70:
    print("Student Failed!")

#10 Create a program that asks for a password input. If it equals "python123", print "Access granted", else "Access denied".
zinebs_password = "python123"
password = input("Enter password: ")

if password == zinebs_password:
    print ("Acess granted!")

else:
    print("Acess denied!")

#3 Loops (for / while)
# Goal: Practice repetition and control flow.

#11. Print all numbers from 1 to 10, all in one single line, using a for loop.
for i in range (1,11,1):
    print(i, end="")

#12 Print all even numbers between 0 and 20 using a for loop.
for i in range (0,21,2):
    print (i, end="")

#OR unsig a if sentence
for i in range (0,21,1):
    if i % 2 == 0:
        print(i, end="")

#13 Write a while loop that prints “Looping…” five times.
i = 0
for i in range (1,6):
    while i <= 6:
        print ("Looping...")
        i = i + 1       # Update i so it eventually ends

#14 Write a while loop that counts down from 5 to 1, then prints “Blast off!”.
i = 5
while i >= 1:
        print ("Blast off!")
        i = i - 1

# 15 Use a loop to calculate the sum of numbers 1 through 100.
summary = []

for i in range (1,101):
    summary.append(i)

print(sum(summary))

#OR
total = 0

for i in range(1, 101):  # 1 through 100 inclusive
    total += i            # add i to the total each time

print(total)

#16 Use a for loop to print each letter in the string "PYTHON"
word = "PYTHON"

for letter in word:
    print (letter, end=",")

#17 Ask the user for numbers until they type 0. Then print the total sum.
while True:
    number = int(input('Enter an integer, exit with "0":'))
    if number == 0:
        print ("Exiting...")

#18 Write a nested loop that prints a 5x5 grid of * characters.
for row in range (5):
    for column in range (5):
        print("*", end="  ")
    print()         # move to next line after each row

#Indexing and Sequences
# Goal: Access data from sequences (lists, tuples, etc.)

#19. Create a list numbers = [10, 20, 30, 40, 50]. Print the first and last element.
numbers = [10, 20, 30, 40, 50]
print (numbers[0], numbers[-1])

#20 Print the third element of the tuple (5, 10, 15, 20)
my_tuple = (5, 10, 15, 20)
print(my_tuple[2])

#21 Create a list of five fruits. Use a for loop to print each fruit.
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    print (fruit)

#22 Use slicing to print the first three elements of [2, 4, 6, 8, 10]
my_list = [2, 4, 6, 8, 10]
print (my_list[0:3])

#23 Create a list of numbers and print the length of the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
print(len(numbers))

#24 Replace the second item in a list with "changed"
my_list = ["apple", "banana", "cherry", "date"]

my_list[1]= "Changed!"
print(my_list)

#25 Loop through a tuple and print each element on one line.
my_tuple = ("apple", "banana", "cherry", "date")

for item in my_tuple:
    print (item, end="")

# 5. Functions
# Goal: Define and call your own functions with parameters and return values.

#26 Write a function greet() that prints "Hello, world!".
def greet():
    print("Hello, World!")

greet()

#27 Write a function add(a, b) that returns the sum of two numbers.
a = int(input("Enter a number for a:"))
b = int(input("Enter a number for b:"))

def add_numbers (a,b):
    summary = a + b
    print (f"{a}+{b} gives you {summary}")

add_numbers(a,b)

#OR without arguments in definition
def add_numbers ():
    a = int(input("Enter a number for a:"))
    b = int(input("Enter a number for b:"))
    summary = a + b
    print (f"{a}+{b} gives you {summary}")

add_numbers()

#28 Write a function is_even(n) that returns True if the number is even, otherwise False.
n = int(input("Enter a number, to test if even!: "))
def is_even (n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(n))

#29 Write a function largest_number(a,b,c) that returns the largest number.
a = 7
b = 8
c = 5

def largest_number(a, b, c):
    return max(a, b, c)

print (largest_number(a,b,c))

#30 Write a function countdown(n) that prints numbers from n down to 1
n = 10
def countdown (n):
    for i in range (n,0,-1):
        print(i)

countdown(n)

# 31. Write a function square_list(nums) that returns a new list of the squares of the given numbers.
nums = [1,2,3,4,5]
def square_list (nums):
    squared_nums = []
    for num in nums:
        num = num ** 2
        squared_nums.append(num)
    return squared_nums

print (square_list(nums))

# 32. Write a function greet_person(name) that returns a string "Hello, <name>!".
name = "Zineb"

def greet_person (name):
    print (f"Hello <{name}>!")

greet_person(name)

# 33. Write a function sum_range(start, end) that returns the sum of all numbers between start and end (inclusive).
start = 20
end = 50

def sum_range (start, end):
    empty_list = []
    for i in range (start,end+1):
        empty_list.append(i)
    return (sum(empty_list))

print(sum_range(start, end))


#6. Sets and Dictionaries (Mappings)
#Goal: Understand how to use sets and key-value pairs.


#34. Create a set with the numbers {1, 2, 3, 3, 2, 1}. Print it — what happens to duplicates?
numbers = {1,2,3,3,2,1}
print(numbers)

#Answer: they dissapear...set only keeps one copy of each unique number.

#35 Create two sets and print their union, intersection, and difference.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print("Union:", union_set, "\nIntersection:", intersection_set, "\nDifference (set1 - set2):", difference_set)

#36 Check whether the number 5 is in {2, 4, 6, 8}.
my_set = {2, 4, 6, 8}
print(5 in my_set)

#37 1. Create a dictionary student = {"name": "Alice", "age": 20, "grade": "A"}. Print the student’s name.
student = {"name": "Alice", "age": 20, "grade": "A"}
# Print the student's name
print(student["name"])

#38 Add a new key "passed": True to that dictionary.
student = {"name": "Alice", "age": 20, "grade": "A"}
student["passed"] = True            # Add a new key-value pair
print(student)          # Print the updated dictionary

#39  Loop through the dictionary and print each key and value.
student = {"name": "Alice", "age": 20, "grade": "A", "passed": True}

for key, value in student.items():      # Loop through dictionary
    print(key, ":", value)

#40 Write a function that takes a dictionary of items and prices, and returns the total cost.
def total_cost(items):
    total = 0
    for price in items.values():
        total += price
    return total

