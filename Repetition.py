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

# Example usage:
shopping_cart = {
    "apple": 2,
    "banana": 1.5,
    "milk": 3
}

print(total_cost(shopping_cart))  # Output: 6.5


#7. Random Module
#Goal: Practice using built-in modules.
#41. Import the random module and print a random integer between 1 and 10.
import random

random_number = random.randint(1,10)
print (random_number)

#42. Create a list of colors and print a random color from the list.
import random
colors = ["red", "blue", "yellow", "black", "pink"]

random_color = random.choice(colors)
print(random_color)

#43. Simulate rolling two dice and printing their total.
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2

print("Die 1:", dice1)
print("Die 2:", dice2)
print("Total:", total)

#44. Write a small guessing game:
#* Random number between 1 and 10.
#* User guesses until correct.
import random
random_number = random.randint(1,10)

while True:
    guess = int(input("Guess the number between 1-10: "))
    if guess < 1 or guess > 10:
        print("Please enter a number between 1-10")
        continue
    if guess == random_number:      #or use elif here and remove the continue from if-statement
        print(f"Correct! The number was {random_number}")
        break
    else:
        print("Wrong number! Try again.")


#8. Classes and Objects
#Goal: Understand how to define and use classes.


#45. Create a class Car with attributes brand and year., crete an instance of the class and print the attributes
class Car:
    def __init__(self, brand, year):
        self.brand = brand  # Brand of the car
        self.year = year    # Year of manufacture

# Create an instance of Car
my_car = Car("Toyota", 2020)

# Access and print the attributes
print("Car brand:", my_car.brand)
print("Car year:", my_car.year)

#46. Add a method display_info() that prints brand and year.
# Define the Car class
class Car:
    def __init__(self, brand, year):
        self.brand = brand  # Brand of the car
        self.year = year    # Year of manufacture

    # Method to display car information
    def display_info(self):
        print(f"Car brand: {self.brand}, Year: {self.year}")

# Create an instance of Car
my_car = Car("Toyota", 2020)

# Call the display_info() method
my_car.display_info()



#47. Create a class Person with name and age. Add a method birthday() that increases age by 1.
# Define the Person class
class Person:
    def __init__(self, name, age):
        self.name = name  # Name of the person
        self.age = age    # Age of the person

    # Method to celebrate birthday
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Create an instance of Person
person1 = Person("Alice", 25)

# Call the birthday() method
person1.birthday()

#48. Create a class BankAccount with methods deposit(amount), withdraw(amount), and get_balance().
# Define the BankAccount class
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance  # Initialize account balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}")

    # Method to check balance
    def get_balance(self):
        return self.balance

# Example usage
account = BankAccount(100)  # Create account with $100
account.deposit(50)          # Deposit $50
account.withdraw(30)         # Withdraw $30
print("Current balance:", account.get_balance())


#49. Create a class Rectangle with width and height and a method to calculate area.
# Define the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width    # Width of the rectangle
        self.height = height  # Height of the rectangle

    # Method to calculate area
    def area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())


#50. Create two Rectangle objects and print which one has a larger area.
# Define the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create two rectangle objects
rect1 = Rectangle(5, 10)
rect2 = Rectangle(8, 6)

# Calculate their areas
area1 = rect1.area()
area2 = rect2.area()

# Compare and print which rectangle has a larger area
if area1 > area2:
    print(f"Rectangle 1 has a larger area: {area1}")
elif area2 > area1:
    print(f"Rectangle 2 has a larger area: {area2}")
else:
    print(f"Both rectangles have the same area: {area1}")

#Common Sequence Functions:
# len(seq)
# min(seq), max(seq)
# sum(seq)
# sorted(seq)
# in, not in

#String Functions (review only if needed):
# str.lower(), str.upper(), str.strip(), str.split(), str.join()

#List Functions:
# list.append(x), list.remove(x), list.pop(), list.sort(), list.reverse()

#Dictionary Functions:
# dict.keys(), dict.values(), dict.items(), dict.get(key), dict.update({...})

#Random Module:
# random.randint(a, b)
# random.choice(seq)
# random.shuffle(seq)
# random.random()
