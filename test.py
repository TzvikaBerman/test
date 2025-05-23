mylist = ["apple", "banana", "cherry"]
print(mylist)
mylist.append("data")
print(mylist)
print(len(mylist))
mylist.remove("apple")
#mylist.pop(mylist.index("apple"))
print(mylist)
mylist.sort()
print(mylist)
myset = {3,1,4,5,1,9}
print(myset)
print(7 in myset)
mytuple = ("dog", "cat", "fish")
print(mytuple) 
print(mytuple[2])
mylist2 = list(mytuple)
print(mylist2)
my2dlist = [[10,20],[30,40]]
print(my2dlist)
my2dlist[1][1]
print(my2dlist[1][1])
print(type(myset))
value = [12,5,8]
value_max = max(value)
print(value_max)
print (max(value))
list_to_reverse = [6,4,2]
list_to_reverse.reverse()
print(list_to_reverse)
copy_list = mylist.copy()
copy_list[0] = 11
print(mylist)
print (copy_list)

def multiply_numbers(num1,num2):
    return num1*num2;

print(multiply_numbers(4,7))

def culculate_square(num):
    return num*num;
print(culculate_square(6))

def calculate_avrage(num):
    return sum(num)/len(num);

#list_nums = [1,2,3,4,5]
#list_avg = calculate_avrage(list_nums)
#print(list_avg)

mynum = [3,4,5]
print(calculate_avrage(mynum))
print (calculate_avrage([1,2,3,4,5,7]))

a = [1,2,3,4]
b = [5,6,7,8]

print (calculate_avrage(a))
print (calculate_avrage(b))
print (calculate_avrage(a) + calculate_avrage(b))


print ('enter your name')
name = input();
print ('hi '+ name)

