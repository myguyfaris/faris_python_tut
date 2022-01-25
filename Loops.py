'''
for loop - defines the start and end point as well as the increment for each iteration
while loop - it keeps looping while a given condition is valid
'''
for number in range(10, 50, 5):
    print(number)
'''
The "number" variable is going to store the values in every iteration, i.e. 1st iteration = 0, 2nd = 1
By default, it starts at 0. You can also define a starting point.
You can also define the increment.
range(starting point, ending point, increment)
'''
name = "Jeffery"
for letter in name:
    print(letter)
else:
    print("The letters were printed out...")
    print("insert whatever here")
'''
The for loop can iterate through the character in the string "jefferey", and print out each character
We can also combine it with if/else statements, you can include as many operations as you want after the for loop
'''

