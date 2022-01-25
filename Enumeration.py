'''
Enumerate - this keyword(function) allows us to use indexes and the values well
'''
for index, value in enumerate(range(5)):
    print(str(index) + " " + str(value))

'''
The for loop above works to churn out the index number, and the value of the number at said index.
The enumerate function allows us to bring both out.
We have to print out the results as string, otherwise it won't be able to concatenate them both.
The empty space in between is just added as a formatting measure
Another example is given below with the world "balaclava"
'''
hat = "Balaclava"
for index, letter in enumerate(hat):
    print(str(index) + " " + str(hat))

'''
We can also store strings in one dimensional arrays
'''
animals = ['cat', 'dog', 'horse', 'Jefferey']
for index, animal in enumerate(animals):
    print(str(index) + ' ' + str(animal))