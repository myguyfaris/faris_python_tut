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
'''
For the while loop above, we first establish that the counter starts at 0. 
And python will first check if counter is equal to 5 and if it isn't, will print counter and increase a step of 1
From there, it loops until the condition in line 9 is met, and the loop is stopped at index 5, which is number 4.
'''