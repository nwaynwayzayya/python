# # Strings and Variables

# # 1. Create an input with a greeting
# print("Hello! \n")
# name = input("Enter your name: ")

# # 2. Ask what their favourite food is
# fav_food = input("What is your favourite food? ")

# # 3. Ask what their favourite hobby is
# fav_hobby = input("What is your favourite hobby? ")

# # 4. Print with a f string of their favourite food and hobby
# print(f"\nYour name is {name}. \nYour favourite food is {fav_food}. \nYour favourite hobby is {fav_hobby}")

# -------------------------------------------------------------------------------------------------------------------------- #

# # Data Types
# num1 = "12345"
# num2 = "67898"
# num3 = "87654"

# # Add num1+num2
# print(int(num1) + int(num2))

# # Add the second number in num1 and the second number in num3
# print(int(num1[1]) + int(num2[1]))

# # Change num2 into a float and print the type to the console as a float
# float_num = float(num2)
# print(type(float_num))

# -------------------------------------------------------------------------------------------------------------------------- #

# Conditionals

# ask the user for the temperature input
# if it's less than 20 degrees you need boots
# if it's less than 30, you need a coat
# if it's less than 70, you need a jacket
# if it's over 78, it is nice outside

# temp = int(input("What is the current temperature? "))

# if temp <= 20:
#     print("You need boots!")
# elif temp <= 30:
#     print("You need a coat!")
# elif temp <= 70:
#     print("You need a jacket!")
# else: 
#     print("It is nice outsice.")



# # -------------------------------------------------------------------------------------------------------------------------- #

# # Functions
# # Input first letter of your name
# # Call a function that adds you first letter to the rest of your name

# def my_function(i):
#     var = i + "yan"
#     print(var)

# my_function(input("what is the first letter of your name? "))


# # -------------------------------------------------------------------------------------------------------------------------- #

# Create a program that calculates the sqft of a room
# Make a function that calculates two parameters that are passed in
# Take an input for width and height as variables
# Call the function and pass in the width and height
# Multiple w * h
# Print the final result

def cal_sqft(w,h):
    print(f"\nThe square feet of the room with width, {w}, and height, {h}, is {w*h}.")

width = int(input("Enter the width of the room: "))
height = int(input("Enter the height of the room: "))

cal_sqft(width, height)