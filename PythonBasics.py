# ignore these lines are they are comments
print("Hello World, let me get good at data science and give me a job!")
# this is a single line comment, made with a hash
"""
This is a multi-line comment, created with triple quotes
"""
# you can assign variables just by defining them as below
num1 = 5
num2 = 0.5
result = num1 * num2
print(result)
"""
num1 is assigned as 5, an integer
num2 is assigned to 0.5, a floating point number
result is assigned to be an operator, where num1 is multiplying num2
from there, we print out the result, 2.5
"""
# you can also assign multiple variables in one line
num3, num4, num5 = 1, 2, 3
result2 = num3 + num4 + num5
print(result2)

# boolean values AKA binary values - it can have 2 output values (TRUE and FALSE)

result3 = 3 < 1

print(type(result3))
print(result3)

'''
result 3 is assigned to be a boolean value, where we set it as 3 being smaller than one
print(type(result3)) will print out the type of value we've assigned in result3
in the console, we can see that it prints <class 'bool'> AKA boolean
the boolean result shows that 3 being smaller than 1, is indeed FALSE
'''
# these boolean values are extremely important in conditional statements
# IF statements look for boolean values
'''
Strings - a chain of characters (or letters), usually written within quotation marks
Strings are one-dimensional arrays or characters. There are no characters in  python - characters are strings
with a single letter
The variable name below is assigned the value "Michael Myers"
We are able to acquire the given letters with given indices (index)
INDICES start with 0, for example, when we print INDEX 0, the letter M is printed
The other way around, can be achieved with -1, AKA the LAST letter of the string
We can also defined a range of indexes, such as index 1 to 5, icha (a substring)
Keep in mind when defining it this way, the final index (5 here) will not be a part of the substring
'''
name = 'Michael Myers'
print(name[0])
print(name[-1])
print(name[1:5])

'''
You can also sum up indices as shown below
We added a space after Michael so that the sum has a space between the first name and last

'''
first_name = 'Michael '
last_name = "Myers"
age = 25
real_age = 84
result4 = first_name + last_name
print(result4)

'''
you can only concatenate(add) same types of data, i.e. you cant concatenate a string with an integer
To show Michaels age, we have to use the format function
The {} bracket is a space to substitute formatted variables in our sentence 
'''
howoldishe = 'Michael is {} years old, bro'
result5 = howoldishe.format(age)
print(result5)

'''
With {}, we can inject as many integers as we want into the sentence
result6 gives us Michaels true age, that lying fuck
'''
howoldishereally = 'He claims to be {}, but Michael is actually {}'
result6 = howoldishereally.format(age, real_age)
print(result6)