#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

print("Enter comma seperated values: ")
data = input()
list = []
for i in data:
    if i == ',' or i == ' ':
        continue
    else:
        list = list + [i]
print(list)
print(tuple(list))
