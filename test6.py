#str1 = input("enter a string: ")
#str2 = input("enter a string: ")
#if str1 == str2:
#    print("the strings are equal: ")
#else:
#    print("the strings are not equal: ")


#num = float(input("Enter a number: "))
#absolute_value = abs(num)
#print("the absolut value is: ", absolute_value)

#num_str = input("Enter a comma-sepereted nambers: ")
#num_list = [float(x) for x in num_str.split(",")]
#max_num = max(num_list)
#print("the maximum number is: ", max_num)

str_num = 123.45
float_num = float(str_num)
print("before", type(str_num))
print("after", type(float_num))

num = 10
str_num = str(num)
print(type(str_num))

my_bool = False
my_int = int(my_bool)
print(my_int)

int_val = input("Enter an intiger: ")
float_num = float(int_val)
print(float_num)

str_list =  ["hello" , "world", "python"]
combine_list = " ".join(str_list)
print(combine_list)

my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
print(my_list)

animals = ["dog", "cat", "mouse"]
print(animals)
animals.append("fish")
print(animals)

numbers = [1,55,24,28,75,94,255,65,32,45,47]
numbers.sort()
print(numbers)

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
combaind_list = list1 + list2
print(combaind_list)

fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "orange"]
fruits.insert(1, "cherry")
print(fruits)
fruits.reverse()
print(fruits)

fruits = ["apple", "banana", "orange", "cherry", "pear"]
new_list = fruits[1:4]
print(new_list)

numbers = [1,2,3,4,5,6,7,8,9]
numbers = sum(numbers)
print(numbers)
print("the sum of the numbers is: ", (numbers))

names = ["tzvika", "sarit" "yehonatan", "ariel"]
shortest_word = min("names", key=len)
print("shortest_word: ", shortest_word)

days_of_ther_week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
first_day = (days_of_ther_week[0])
last_day = (days_of_ther_week[-1])
print(first_day)
print(last_day)

tuple1 = (1,2,3)
tuple2 = (4,5,6)
reversed_tuple = (tuple2 + tuple1)
print(reversed_tuple)

my_tuple = (1,2,5,8,5,3,4,2,6,2,2,8,5)
count_of_2 = my_tuple.count(2)
count_of_8 = my_tuple.count(8)
print(count_of_2)
print(count_of_8)

my_tuple = ([1,0],[10,30])
print(my_tuple)

my_list = [10,20,30,40,50]
my_tuple = tuple(my_list)
print(my_tuple)