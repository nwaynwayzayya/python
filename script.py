#New Line function
def nl():
    print('\n')

#Boolean expressions (True or False)
print("Boolean expressions:")

boo1 = True
boo2 = 3 * 3 == 9
boo3 = False
boo4 = 3 * 3 != 9

print(boo1, boo2, boo3, boo4)
print(type(boo1))

nl()
#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 == 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

nl()
#Conditional Statements
def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "NO drink for you!"
    
print(drink(3))
print(drink(1))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else: 
        return "You're too poor and too young."
    
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))


nl()
#Lists - Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0])  #return the first item in the list
print(movies[1])  #return the second item
print(movies[1:3]) #return the list starting at one and stops before 3
# Output: 'The Hangover', 'The Perks of Being a Wallflower'
print(movies[1:4])  #return all after the second item to the last item
print(movies[1:])  #return the same as the one above [1:4]
print(movies[:1])  #Output: 'When Harry Met Sally'
print(movies[-1])  #return the last item

print(len(movies)) #return the number of items in a list
movies.append('JAWS')  #append to the end of the list
print(movies)

movies.pop()  #delete the last item of the list
print(movies)

movies.pop(0)  #delete the first item of the list
print(movies)

nl()
# Tuples
# Unlike lists -- tuples can't be modified -- immutable
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
# Looping

# For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print (x)

# While loops - execute as long as true

i = 1
while i < 10:
    print(i)
    i += 1
