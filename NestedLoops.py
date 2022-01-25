'''
we can use multiple loops inside other loops - and these are called nested loops
'''

for outer_index in range(5):
    for inner_index in range(3):
        print("outer index: " + str(outer_index) + " inner_index:" + str(inner_index))

"""
What happens here is that the inner_index loop has to be completed first (0 1 2), before the outer_index loop can 
continue until completion (0 1 2 3 4). 
Line 6 is considered as a nested loop. 
"""