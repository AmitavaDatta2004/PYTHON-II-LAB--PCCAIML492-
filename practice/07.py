with open("file.txt","r") as file:
    data=file.read().split("\n")

print(data)

if data[0].startswith("P"):
    print(data[0])