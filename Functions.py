#Functions


# def hello():
#     print("Hello, World!")
    
# hello()

# def farenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5.0/9.0
#     return celsius

# temp_in_celsius = farenheit_to_celsius(100)
# print("Temperature in Celsius:", temp_in_celsius)

# def add_numbers(a,b):
#     return a+b

# result = add_numbers(5, 7)
# print("Sum:", result)



# def get_greeting():
#     return "hell0 there"

# greeting = get_greeting()
# print(greeting)


# def my_function(animal , name ):

#     print("I have a " + animal + " named " + name)
# my_function("dog", "Buddy")

# *args and *kwargs

# def display_info(*args):
#    print("Positional arguments:", args[2])

# display_info("apple", "banana", "cherry")


#pyhton scope

# def my_func():
#     x = 10
#     print("Value of x inside the function:", x)
    
# my_func()

# def myfunc():
#     x=300;
#     def innerfunc():
#         print(x)
#     innerfunc()
# myfunc()


# Global Scope

# x = 50

# def myfunc():
#     print(x)
# myfunc()

# print(x)



# def myfunc():
#     global y
#     y = 100
#     print(y)
    
# myfunc()


x = "global x"


def outer_function():
    x= "enclosing x"
    def inner():
        x = "local x"
        print("Inner:", x)
    inner()
    print("Outer:", x)
    
outer_function()
print("Global:", x)