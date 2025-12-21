

thislist = ["rock", "paper", "scissors", "hello", "world"]
print(thislist)

print(len(thislist))  #length of the list

list1 =["abc" , 34 , True , 40 ]
print(list1)

print(type(thislist))  #data type of the list  

print(thislist[0])  #accessing elements in the list   

thislist.sort()  #sorting the list
print(thislist)

thislist.sort(key=str.lower)  #sorting the list without case sensitivity
print(thislist)