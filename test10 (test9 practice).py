total = 0
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        total += num
print("sum", total)

text = input("enter a string: ")
reversed_text = ""
i = len(text)-1
while i >=0:
    reversed_text += text[i]
    i  -= 1
print("reversed string: ", reversed_text)

list_of_words = ["apple", "banana", "orange", "apple", "banana", "apple"]
word_counts = {}
for word in list_of_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "d": 3, "e": 4}
common_elements = {}
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        common_elements[key] = dict1[key]
print(common_elements)

data = {"a": 10, "b": "Hello", "c": 20, "d": 30, "e": "world"}
total = 0
for value in data.values():
    if isinstance(value, int):
        total += value
print(total)

sentence = "this is a sample sentence. this is another sentence."
word_freq = {}
words = sentence.split()
for word in words:
    if word in word_freq:
        word_freq[word] +=1
    else:
        word_freq[word] = 1
print(word_freq)

        