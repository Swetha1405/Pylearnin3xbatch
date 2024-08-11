# ✅ 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
def is_leap_year(year):
    if (year%4==0 and year%100!= 0) or (year%400==0):
        return True
    else:
        return False

year=int(input("Enter the year: "))
if is_leap_year(year):
    print(year,"is leap year")
else:
    print(year, "is not a leap year")
# # -----------------------------------------------------------------------------
#
# # A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# #
# # Use an if-else statement to make this determination.
#
# #
# #
# # Input = 2024
# #
# # Output = Leap year
# # ------------------------
# # ✅ 2. Triangle Classifier:
# # Write a program that classifies a triangle based on its side lengths.
# #
# #
# #
# # Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# #
side1=float(input('Enter the side1: '))
side2=float(input('Enter the side2: '))
side3=float(input('Enter the side3: '))
if side1==side2==side3:
    print("Triangle is Equilateral")
# elif (side1==side2) or(side1==side3) or (side2==side3):
#     print ("triangle is isosceles")
elif (side1==side2!=side3) or (side3==side1!=side2) or (side2==side3!=side1):
    print("triangle is isosceles")
else:
    print("triangle is scalene")
#
# #
# #
# # Use an if-else statement to classify the triangle.
# #-------------------------------------------
# # 3 Input
# #
# # side 1, side 2 and side 3
# #
# # output - Eq, Iso, Scalene -
# #
# # Eq. = side 1 == side 2 = side 3
# #
# #
# #
# #
# #--------------------------------------
# # ✅ Task - Fibonacci series and Factorial
#
#
# # 3. Factorial
#
import math

number = int(input("Enter a number to calculate its factorial: "))

factorial = math.factorial(number)

print("Factorial of", number, "is", factorial)
# n = 5

# 5! -->5*4*3*2*1 -> 120

# 3! -> 3*2*1 -> 6

# 4! -> 4*3*2*1 -> 24



# ✅ #4. Fibonaci series
# 0,0+1, 0+1+1,


n = 7
num1 = 0
num2 = 1
next_number = num2
count = 0

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
# n = 7

# 0, 1, 2, 3, 5, 8, 13