'''
Calculating the average of the first 10 items starting with 1
'''
number_list = 0
numerator = 0

for denominator in range(1, 11):
    numerator += denominator
    denominator += 1
    print("The average of the first 10 items (starting with 1) is " + str(numerator/denominator))