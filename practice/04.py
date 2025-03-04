with open("file.txt","r") as file:
    data=file.read()

list=data.split()
print(list)


newlist=[]
newlist1=[]
for i in list:
    newlist1.append(sorted(i))
    newlist.append("".join(sorted(i)))


print(newlist1)
print(newlist) 

set=set(newlist)
print(set)

anagram=0
for i in set:
    if newlist.count(i)>1:
        anagram+=newlist.count(i)

print(anagram)