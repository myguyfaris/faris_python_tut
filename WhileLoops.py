'''
While loop - it keeps looping while a given condition is valid
'''
name = "Kevin"
age = 24
letter_index = 0
while letter_index < len(name):
    print(name[letter_index])
    letter_index = letter_index + 1
else:
    print("Finished with the while loop")
'''
line 4 - we define the name with a string "Kevin"
line 5 - we define letter_index as 0, given that we want the first character
line 6 - define the while loop, where letter_index is less than length(number)
of characters in name, you print it out. A number would do fine here, but an error would pop out
if the name changes, say from Kevin(5 characters) to Rob (3). So we use the len function

line 7 - From there, you print out name - relative to letter index, and then you redefine letter_index
by giving it an increment of 1. 

line 8 - After that, the loop repeats itself until letter_index 6, 
where there is no more character to print

So as long as the condition is met in line 6, the loop will keep running operations within the while loop

If all conditions are met, we can end it with the else statement
'''
counter = 0

while counter < 10:
    print(counter)
    counter = counter + 2
else:
    print("counter while loop ended")

'''
Same thing as above, but this time, we define counter as a number 0, and the while loop will list out all numbers
lower than 10 at a step size of 2.
'''
