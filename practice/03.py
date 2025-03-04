with open("file.txt","r") as file:
    data1=file.read()


with open("duplicate.txt","r") as file:
    data2=file.read()


if(data1==data2):
    print("Files are same")
else:
    print("Files are different")