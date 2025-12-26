# ========================================
# PYTHON INPUT & OUTPUT BASICS
# ========================================

# ----- OUTPUT with print() -----

# Simple output
print("Hello World")

# Print multiple items
print("Python", "is", "fun")

# Print with separator
print("apple", "banana", "cherry", sep=" - ")

# Print without newline at end
print("Same line: ", end="")
print("continued here!")


# ----- INPUT with input() -----

# Taking text input
name = input("What is your name? ")
print("Hello,", name)

# Taking number input (convert string to int)
age = input("How old are you? ")
age = int(age)  # Convert to integer
print("In 5 years, you'll be", age + 5)

# Taking decimal number input
price = input("Enter a price: ")
price = float(price)  # Convert to decimal
print("With 10% tax:", price * 1.10)


# ----- FORMATTED OUTPUT (f-strings) -----

# f-strings - the modern way to format output
username = "Anuska"
score = 95
print(f"Player {username} scored {score} points!")

# Calculations inside f-strings
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} x {b} = {a * b}")
