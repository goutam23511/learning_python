#removing all the duplicates in the list 

list=[1,3,4,53,23,35,6,84,4,2,1,2,2,2,3,4,5,6,7]
new=[]

for i in list:
    if i not in new:
        new.append(i)

print(new)