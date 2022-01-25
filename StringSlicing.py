'''
We are going to use integers (numbers) as strings (text)
We'll define s as a string containing numbers, and we'll pull out each
number through indexes
Python stores the string as an array of characters
'''

s = '0123456789'
'''
We can use rounded brackets [] to pull out a character through their index
'''
print(s[4])
'''
From there, we can perform string slicing with the colon, : operator
Python then prints out the substring 0123456
Indexes always start from 0 unless defined
If we do not define the last index, then Python will give the last index too
If we do not define any index, Python will return whole string, including first and last
'''
print(s[0:7])
print(s[:])
'''
We can define the step size too
In the case below, we'll go from index 0 to 10, with a step size of 2
Python prints out 02468
'''
print(s[0:10:2])
'''
Positive step size = left to right
Negative step size = right to left (but you'll have to reverse the index)
'''
print(s[10:0:-2])
'''
Therefore, to reverse the string, you can introduce a step size of -1
'''
print(s[::-1])
'''
It works for text too, for example:
'''
p = 'Eat my ass my guy hahaha'
print(p[::-1])