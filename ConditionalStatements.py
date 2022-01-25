'''
Conditional statements are features of a programming language that perform
different actions whether a condition is true or false.
This condition is a boolean variable (binary flag, true or false)
'''
num = 5000

if num < 500:
    print("The number is smaller than 500")
else:
    print("The number is not smaller than 500")
'''
The if condition above is defined to a boolean value (num<500)
If true, will print out first string
If false, triggers else, and will print out second string
You can have multiple commands in the if and else statements
'''
'''
You can use the built in input function to enable user input
From there, you have to change the string input to whatever variable type
you want, in this case, integers because we're doing math
And then use a combination of if, else, elif (else if), and, or conditions
'''
numb = input("Yo give me a number divisible by 2 and 5:")
numb = int(numb)
if numb % 2 == 0 and numb % 5 == 0:
    print("Cheers my guy, very much appreciated")
else:
    print("you cant take orders can you, you dip?")



