'''
Type casting - sometimes we want to specify the type of variable
Python is an object oriented language AKA OOP Object Oriented Programming
Python defines data types with classes
type casting transforms inputs into any data type you like
'''
a = int('23')
b = str(23.5)
print(a)
print(type(a))
print(b)
print(type(b))
'''
Above, we defined a to be a string 23 as an integer, so when we print a, it returns
a value of 23, and tell us the data class is an integer
But in b, we defined the integer 23.5 as a string, and it prints out 23.5 as a string
'''
c = int(23.5)
print(c)
print(type(c))
c2 = float(23)
print(c2)
print(type(c2))
'''
If the value is a float (say, 23.5), python will round it down
To fix that, use the float() function, like in c2
You can do the same with a string too
'''