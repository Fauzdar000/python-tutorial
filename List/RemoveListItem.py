thislist = ["rock", "paper", "scissors"]
thislist.remove("paper")  #removing an item by value
print(thislist)


#removing an item by index
thislist = ["rock", "paper", "scissors"]    
thislist.pop(1)
print(thislist)


#removing the last item
thislist = ["rock", "paper", "scissors"]        
thislist.pop()
print(thislist)


#deleting an item by index
thislist = ["rock", "paper", "scissors"]        
del thislist[0]
print(thislist)

#deleting the entire list
thislist = ["rock", "paper", "scissors"]
del thislist
#print(thislist)  #this will raise an error because the list no longer exists
#clearing the list
thislist = ["rock", "paper", "scissors"]
thislist.clear()
print(thislist)
print(len(thislist))  #length of the cleared list
