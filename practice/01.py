list=["hi","hello","how","are","you"]

with open('file.txt','w') as file:
    file.writelines("\n".join(list))