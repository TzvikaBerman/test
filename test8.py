my_str = "3.14159"
print(type(my_str))
print(float(my_str))
print(type(float(my_str)))

my_int = 42
my_str = str(my_int)
print(my_str)
print(type(my_str))

my_bool = True
int_true = int(my_bool)
print(my_bool)
print("value: ", int_true)
print(type(my_bool))

my_float = float(input("Enter a number: "))
rounded_number = round(my_float)
print(rounded_number)

my_tuple = ("cherry", "banana", "apple")
my_list = list(my_tuple)
print(my_list)

num = 200
hex_str = str(num)
print("hex string:", hex_str)

countries = ["Israel", "Usa", "Russia"]
print(countries)
countries.insert(0, "England")
print(countries)
countries.append("Japan")
print(countries)

list1 = ["tzvika", "ariel", "yehonatan"]
list2 = ["sarit", "arial", "kaya", "sarit"]
uniqe_list = list(set(list1+list2))
print("uniqe_list: ", uniqe_list)

num = float(input("Enter a number: "))
if num > 0:
    print("the number is possitive: ")
elif num < 0:
    print("the number is negative: ")
else:
    print("the number equ 0")


num = int(input("Enter a num: "))
if num %  2 == 0:
    print("The number us even")
else:
    print("The number is odd")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("the largest number is: ", largest)

char = input("Enter a char: ")
if char.lower() in "aieou":
    print("the char is a vaule: ")
else:
    print("the char is consosant: ")

string = input("Enter a stirng: ")
if string == string [::-1]:
    print("the string is a pilandrom")
else:
    print("the string is not a pilandrom")    

precentege = float(input("Enter a precentege: "))
if precentege >= 90:
    grade = "A"
elif precentege >= 80:
    grade = "B"
elif precentege >= 70:
    grade = "C"
elif precentege >= 60:
    grade = "D"
else:
    grade = "F"

print("the grade is: ", grade)

year = int(input("Enter a Year: "))
if year % 100 == 0:
    print("the year is a centuey")
else:
    print("the year is not a century")


