with open("file.txt","r") as file:
    data=file.read()


with open("duplicate.txt","w") as file:
    file.write(data)