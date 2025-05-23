'''# this is a single-line comment

file = open("data.txt","r")

content = file.read(100)

file.close()'''

'''try:
    file = open("filenotfound.txt", "r")
except:
    FileNotFoundError
print("file no found")

with open("output.txt", "w") as file:
    file.write("Hello World!")

try:
    result = 5 / 0
except: ZeroDivisionError
print("Cannot dvide by Zero.")

with open("my_file.txt", "r+") as file:
    file.write("new data")

with open("text_data.txt", "w") as file:
    file.write("this is some text data")'''

def safe_divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "cannot divide by zero"

