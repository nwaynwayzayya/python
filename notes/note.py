# #Strings and Variables
# print("Hello World!")
# print("Hello World! \nHello World #2!")
# print("Hello" + " " + "World!")

# name = "Jim"
# print(name)

# #Asking for User input
# name = input("What is your name? ")

# #Printing a string with a variable inside the string
# print(f"Hello {name}")

# #Print the alphabet in that particular number
# name = "Tommy"
# print(name[2])

#-----------------------------------------------------------------------------------------------------------------------------#

#Data Types
# string = "my string"
# int = a number 7
# float = number with a ".", example: 3.14
# boolean = true / false

# Checking the data type of a variable
# float_num = float(123)
# int_num = int(123.4)
# string_word = str(1234)

# print(type(float_num))
# print(type(int_num))
# print(type(string_word))

# print(12 + "12")  # Can't add because those are two different data types
# print("12" + "12")  # Outputs '1212' because we're adding two strings here(NOT integers)
# print(12 + int("12"))  # Outputs 24

# -------------------------------------------------------------------------------------------------------------------------- #

# Conditionals

# If you are under 5, you are a kid
# If you are 5-15, you are a big kid
# If you are 15-21, you are a bigger kid
# If you are over 21, you are old

# var = int(input("What is your age? "))

# if var <= 5:
#     print("You are a kid!")
# elif var <= 15:
#     print("You are a BIG kid!")
# elif var <=21:
#     print("You are a bigger kid!")
# else:
#     print("You are old")

# -------------------------------------------------------------------------------------------------------------------------- #

# For Loops

# string = "hello World!"
# for i in string:
#     print(i)

# -------------------------------------------------------------------------------------------------------------------------- #

# Lists

# my_list = ["item1", "item2", "item3"]

# for i in my_list:
#     print(i)



# -------------------------------------------------------------------------------------------------------------------------- #



# While loops

# on = True
# i=0

# while on:
#     var = input("Continue running while loop. y or n? ")
#     i += 1
#     if var == "n":
#         on = False



# -------------------------------------------------------------------------------------------------------------------------- #



# Functions
def my_function():
    print("It worked")

my_function()

# passing parameters
def my_function2(i):
    var = i + 3
    print(var)

my_function2(input("what would you like to add 3"))


