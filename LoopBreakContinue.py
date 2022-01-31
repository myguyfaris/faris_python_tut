'''
In computer science - a loop is a programming structure that repeats a sequence of instructions until a specific
condition is met.
1. break: we can stop the given loop before it has looped through all the items
2. continue: we can skip(stop) the actual iteration of a loop and continue with the next iteration
'''
counter = 0
while counter < 10:
    if counter == 5:
        break
    print(counter)
    counter = counter + 1
print("The while loop is finished")
'''
For the while loop above, we first establish that the counter starts at 0. 
And python will first check if counter is equal to 5 and if it isn't, will print counter and increase a step of 1
From there, it loops until the condition in line 9 is met, and the loop is stopped at index 5, which is number 4.
'''
number = 0
while True:
    if number == 100:
        break
    print(number)
    number = number + 1
print("the loop is done after reaching 100")
'''
For the while loop above, True (in this case, is always true), then the loop will run infinitely.
So for that, we'll have to introduce the condition if number == 100 so that it stops there, and the loop can be broken
'''

for stuff in range(0, 10, 1):
    if stuff == 5 or stuff == 6 or stuff == 7:
        continue
    print(stuff)
print("The while loop is finished")
'''
For continue above, rather than break and stopping the loop, it skips the iteration where the condition is met, and 
proceeds on to the next iteration.
'''