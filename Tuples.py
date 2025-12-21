
names=("Alice", "Bob", "Charlie")

names[0]  # Accessing the first element
names[1]  # Accessing the second element

names.index("Bob")  # Finding the index of "Bob"
print(names.index("Bob"))

print(sorted(names))  # Sorting the tuple (returns a list )

new_names = names + ("Diana",)  # Concatenating tuples
print(new_names)