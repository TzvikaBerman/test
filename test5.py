my_var = -10
print(my_var)
print(type(my_var))

my_float = 3.14
print(my_float)
print(type(my_float))

my_string = "12345" 
print(my_string)
print(type(my_string))

my_bool = False
print(my_bool)
print(type(my_bool))

none_var = None
print(none_var)
print(type(none_var))

int_var = 5
float_var = 2.5

int_var_to_float = float(int_var)
print(int_var_to_float)

float_var_to_int = int(float_var)
print(float_var_to_int)

my_bool = True
str_var = str(my_bool)
print(type(str_var))

my_float = 7.8
my_int = int(my_float)
print(my_int)

my_float = 7.8
rounded_int = int(round(my_float))
print(rounded_int)

int_var = 123
str_var = str(int_var)
print(str_var)
print(type(str_var))
str_var = int(str_var)
print(str_var)
print(type(str_var))

my_string = "its a beutiful day"
print(len(my_string))

name = "Tzvika"
age = "43"
hight = "1.79"

sentence = (f"my name is " + (name), "my age is " + (age), "and my hight is " + (hight))
print(sentence)

my_age = input("Enter your age:")
print(my_age)
print(type(my_age))

my_sentence = "its a beutiful day"
first_car = my_sentence[0]
print(first_car)
last_car = my_sentence[:-1]
print(my_sentence)

every_second_caracter = my_sentence[::2]
print(every_second_caracter)

mystr1 = input("enter the first string:")
mystr2 = input("enter the second string:")
combined_str = mystr1 + " " + mystr2
print(combined_str)

dirty_str = "     Hello world!"
print(dirty_str)
clean_str = dirty_str.strip()
print(clean_str)

main_string = "nice to meet you"
words = main_string.split()
print(words)
first_word = words[0]
print(first_word)
last_word = words[-1]
print(last_word)

main_str = "nice to meet you"
reversed_Str = main_str[::-1]
print(reversed_Str)

full_name = input("Enter your full name: ")
print(full_name)
first_char_first_name = full_name[0]
first_char_last_name = full_name[7]
short_name = first_char_first_name + first_char_last_name
print(short_name)

main_domain = input("Enter a domain: ")
split_domain = main_domain.split(".")
print(split_domain)
word1 = split_domain[0]
word2 = split_domain[-1]
print(word1)
print(word2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
average = (num1 + num2) / 2
print("the average is: ", average)

length = float(input("enter length: "))
width = float(input("enter width: "))
area = (length * width)
perimeter = (length * width) * 2
print("the area is: ", area)
print("the perimeter is: ", perimeter)