my_string = "Hello World!"
print(type(my_string))

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum_result = num1+num2
print(sum_result)

my_float = 3.14
print(type(my_float))

my_bool = True
print(type(my_bool))

my_string = "Python"
char_t = my_string[2]
print(char_t)

num1 = 2.5
num2 = 3.5
product_result = num1*num2
print(product_result)

name = "tzvika "
massege = name + "is a python programmer"
print(massege)

my_float = 7.8
my_int = int(my_float)
print(my_int)

my_integer = 42
result = my_integer + 7
print(result)

sentence = "this is a sample sentence"
word = sentence[10:16]
print(word)

my_list = ["apple", "banana", "cherry"]
print(my_list)

my_list = ["apple", "banana", "cherry"]
my_list.append("date")
print(my_list)

my_list = ["apple", "banana", "cherry"]
my_list.append("date")
my_list.remove("apple")
print(my_list)

my_list = ["apple", "banana", "cherry"]
my_list.append("date")
my_list.sort()
print(my_list)

my_set = {3,1,4,1,5,9}
print(my_set)

my_set = {3,1,4,1,5,9}
contain_num_7 = 7 in my_set
print(contain_num_7)

animals = ("dog", "cat", "fish")
print(type(animals))

animals = ("dog", "cat", "fish")
print(animals[2])

animals = list[("dog", "cat", "fish")]
print(animals)

my_2d_list = [[10,20], [30,40]]
print(my_2d_list)

my_2d_list = [[10,20], [30,40]]
value_40 = my_2d_list[1][1]
print(value_40)

value = [12,5,8]
max_value = max([12,5,8])
print(max_value)

numbers = [6,4,2]
reversed_order = [6,4,2][::-1]
print(reversed_order)

def multiplay_numbers (num1, num2):
    return num1 * num2
result = multiplay_numbers(5, 7)
print(result)

def calculate_square(number):
    return number * number

result = calculate_square(6)
print(result)


total = 0
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        total += num
print("sum", total)

text = input("Enter a text: ")
reversed_text = ""
i = len(text) -1
while i>=0:
    reversed_text += text[i]
    i -= 1
print("reversed_string", reversed_text)



