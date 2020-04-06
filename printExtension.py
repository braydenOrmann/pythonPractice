#Write a Python program to accept a filename from the user and print the extension of that.

print("Enter a file name with its extension: ")
file = input()
count = 0
for i in file:
    if i == '.':
        break
    else:
        count += 1
print(file[count+1:])
