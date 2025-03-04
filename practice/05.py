with open("file.txt", "r") as file:
    words = file.read().split()
    print(words)

list = []
for i in words:
    if i not in list:
        list.append(i)

with open("file.txt", "w") as file:
    for i in list:
        file.write(i + " ")