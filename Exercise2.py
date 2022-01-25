'''
Calculating the average of the first 10 items starting with 1
'''
number_list = 0
numerator = 0

for denominator in range(1, 11):
    numerator += denominator
    denominator += 1
    print("The average of the first 10 items (starting with 1) is " + str(numerator/denominator))

'''
create an object starting from zero, create the numerator object too
start the loop for denominator, beginning from 1 to 11 (as it stops counting at 10)
establish numerator rule 
establish denominator step increase
print result average = numerator divided by denominator
'''