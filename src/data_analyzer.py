import sys
from utils import greet

# Variables
name = "Jess"
age = 22
numbers = [1, 2, 3, 4, 5, 6]
person = {"name": "Jess", "age": 22}
fruits = ("apple", "banana", "cherry")


print("Variables:")
print(name, age, numbers, person, fruits)
print(fruits)
print("-" * 40)
# Conditionals
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")
print("-" * 40)

# Loops
print("For loop with range:")
for i in range(5):
    print(i)

print("While loop:")
count = 0
while count < 3:
    print("Count is", count)
    count += 1
print("-" * 40)
# Built-in functions
numbers = [1, 2, 3, 4, 5]

print("Using enumerate:")
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")

print("Using id (memory address):")
print("id of numbers list:", id(numbers))
print("-" * 40)

# String to int casting
num_str = "42"
num_int = int(num_str)
print("Casting string '42' to int:", num_int + 10)
print("-" * 40)
# Using imported function
print(greet(name))
print("-" * 40)

# Command Line Arguments
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Command line arguments received:")
        for i, arg in enumerate(sys.argv):
            print(f"Arg {i}: {arg}")
    else:
        print("No command line arguments provided.")
