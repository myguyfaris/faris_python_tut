'''
Fibonacci numbers is a sequence such that each number is the sum of the two preceding numbers, so the first few is
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 etc such as that
F0 = 0, F1 = 1,
Fn = Fn-1 + Fn-2
for n>1
'''

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b
'''
What we're trying to do above is to list out fibonacci numbers under 100
So we define the first two fibonacci numbers, a = 0 and b = 1 
Define the condition, i.e. first number a is below 100,
print out a
redefine the two numbers according to formula in line 5
'''
