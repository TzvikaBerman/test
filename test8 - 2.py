num = int(input("Enter a number: "))
if num > 0:
    print("number is possitive")
elif num < 0:
    print("number is negative")
else:
    print("number equils 0")  


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("the largest numbner is:", largest)

char = input("Enter a char: ")
if char.lower() in "aieou":
    print("the char is vowel")
else:
    print("the char is consonant")

grade = float(input("Enter a grade: "))
if grade > 90:
    grade = "A"
elif grade > 80:
    grade = "B"
elif grade > 70:
    grade = "C"
elif grade > 60:
    grade = "D"
else:
    grade = "F"
print("the grade is", grade)

year = int(input("Enter a Year: "))
if year % 100 == 0:
    print("year is a century")
else:
    print("year is not a century")

