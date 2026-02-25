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
print("12" + "12")  # Outputs '1212' because we're adding two strings here(NOT integers)
print(12 + int("12"))  # Outputs 24