#Dictionaries in Python

dog = {
    "name": "Buddy",    
    "age": 5,
    "breed": "Golden Retriever",
}



print(dog);
print(dog["name"])  # Accessing value by key    
print(dog["age"])   # Accessing another value by key        

dog["age"] = 6  # Modifying an existing value
print(dog["age"])

print(dog.get("breed"))  # Using get() method to access value   
print(dog.keys())    # Getting all keys
print(dog.values())  # Getting all values   

print(dog.pop("age"))  # Removing a key-value pair
print(dog)

print(dog.popitem())  # Getting all key-value pairs as tuples

print(list(dog.items()))  # Getting all key-value pairs as tuples

dog["favorite_toy"] = "Ball"  # Adding a new key-value pair
print(dog)

