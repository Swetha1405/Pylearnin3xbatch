# Task #1
# Explain the difference between the = operator and the == operator in Python.
# In Python, the '=' operator is the assignment operator. It's used to assign a value to a variable.
#
# ex: x=2
#
#  the '==' operator is the equality operator. It's used to compare two values to see if they are equal.
# x == 5
# This expression evaluates to True if the value of x is equal to 5, and False otherwise.
#
# '=' is used to assign values, '==' is used to compare values for equality.
# ---------------------------------------------------------------------------------
# # What does the ** operator do in Python, and how is it used?
# # ** is used to to power the value , ex: 2**2=4,2**4=16
# ------------------------------------------------------------------------------
# # What does the ^ operator do in Python, and in what context is it commonly used?
# #
# # the '^' operator is the bitwise XOR (exclusive OR) operator. It performs the XOR operation between corresponding bits of two operands. Here's how it works:
# # If both bits are the same, the result is 0.
# # If both bits are different, the result is 1.
# ----------------------------------------------------------
#
#
#
#
#
# Task #2
# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
num = int(input("Enter the num "))
square=num**2
cube=num**3
print("Square of",num, "is",square)
print("cube of",num, "is",cube)

# # Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1=int (input("Enter the num1 "))
num2=int (input("Enter the num2 "))
num3=int (input("Enter the num3 "))
if num1>num2  and num1>num3:
    print(num1 ,"is greater than" ,num2 ,"and", num3)
elif num2>num1 and num2>num3:
    print(num2 ,"is greater than" ,num3 ,"and", num1)
else:
    print(num3, "is greater than", num2, "and", num1)
