friends_list = ["tzvika","yehonatan", "ariel"]
print(type(friends_list))

my_tuple = (3,5,0.5,0.8)
print(type(my_tuple))

animals = {"dog": "כלב", "cat": "חתול", "bird": "ציפור"}
print(type(animals))

my_str = ("its a beutiful day")
print(type(my_str))

my_bool = True
my_str = (my_bool)
print(type(my_str))

my_int = 350
my_float = float(my_int)
print(my_float)
print(type(my_float))

my_float = 30.45
my_int = int(my_float)
print(my_int)
print(type(my_int))

nothing = None
print(nothing)
print(type(nothing))

numbers = [1,2,3,4,5,6,7]
my_tuple = tuple(numbers)
print(my_tuple)
print(type(my_tuple))

my_email = "zvika@gmail.com"
print("username:", my_email.split("@")[0])
print("domain:",my_email.split("@")[1])

comma_separeted = "apple, banana, cherry"
word_list = comma_separeted.split(",")
print(word_list)

test_string ="tzvika"
if test_string[0] == test_string[-1]:
    print("first latter and last lattae are the same")
else:
    print("first lattar and last lattar not the same")

test = "abababa"
if test[0] == test[-1]:
    print("start and finish with the same latter")
else:
    print("start and finish not the same latter")


birthday = "09/12/1981"
day, month, year = birthday.split("/")
print("day:", day, "month:", month, "year", year)


text = (input("enter a text:"))
char_to_count = "a"
count = text.count(char_to_count)
print(count)

my_str = "have a nice day"
print("uppercase:", my_str.upper())
print("lowercase:", my_str.lower())

my_string = "12345aaaa"
if my_string.isdigit():
    print("my_string contains only digits")
else:
    print("my_string not contains only dgits")

my_string1 = input("Enter a text: ")
my_string2 = input("Enter a text: ")
if len(my_string1) > len(my_string2):
    print("stirng1 is longer then my_string2")
elif len(my_string2) >len(my_string1):
    print("my_string2 is longer then my_string1")
else:
    print("both strings are equal")

text = "this is a test"
if " " in text:
    print("text contains spaces")
else:
    print("text not contains speces")

num1 = float(input("Enter a num: "))
num2 = float(input("Enter a num: "))
print("sum:", num1+num2)
print("diff:", num1-num2)
print("multiplay", num1*num2)
print("div", num1/num2)

length = float(input("Enter a length: "))
width = float(input("Enter a width: "))
area = (length * width)
perimeter = (length + width) * 2
print("the area is: ", area)
print("the perimeter is: ", perimeter)

word1 = input("Enter a word: ")
word2 = input("Enter a word: ")
text = (word1 + " " + word2)
print(text)

