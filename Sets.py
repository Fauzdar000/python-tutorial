#sets

# A set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
# Python's set class represents the mathematical notion of a set.
# Sets are used to store multiple items in a single variable.
# Sets are created using curly braces {} or the set() function.
# Example of a set

set1 = {"apple", "banana", "cherry"}
set2 ={"orange"}

mod = set1.union(set2) #modifying set1 by adding set2 elements
print(mod)

# Example of a set with mixed data types
set3 = {1, 2.5, "hello", (1, 2, 3)}
print(set3)