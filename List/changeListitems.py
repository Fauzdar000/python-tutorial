thislist =["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #changing item value
print(thislist)


thislist =["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #changing a range of item values
print(thislist)


thislist =["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #inserting item at a specific index
print(thislist)

thislist =["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  #adding items from another list
print(thislist)